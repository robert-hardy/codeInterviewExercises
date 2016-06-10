import sqlite3 as sqlite

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE product
        (
            product_id NUMBER PRIMARY KEY,
            name varchar2(128) NOT NULL,
            rrp NUMBER NOT NULL,
            available_from DATE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE client_order
        (
            order_id NUMBER PRIMARY KEY,
            product_id NUMBER NOT NULL,
            quantity NUMBER NOT NULL,
            order_price NUMBER NOT NULL,
            dispatch_date DATE NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        );
    """)
    conn.commit()


def populate_product_table(conn, rows):
    query = """
        INSERT OR IGNORE INTO product
        VALUES (?, ?, ?, ?)
    """
    populate_table(conn, query, rows)


def populate_order_table(conn, rows):
    query = """
        INSERT OR IGNORE INTO client_order
        VALUES (?, ?, ?, ?, ?)
    """
    populate_table(conn, query, rows)


def populate_table(conn, query, rows):
    cur = conn.cursor()
    try:
        cur.executemany(query, rows)
        conn.commit()
    except:
        raise


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


def initialize_db(filename):
    # These first two lines mean that we will get rows back as dicts and
    # dates as Python datetime.date objects.
    conn = sqlite.connect(filename, detect_types=sqlite.PARSE_DECLTYPES)
    conn.row_factory = dict_factory
    create_tables(conn)
    return conn

def get_books_that_are_not_selling_well(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT client_order.product_id, SUM(quantity) as total_sold
        FROM
            client_order JOIN product
            ON client_order.product_id = product.product_id
        WHERE julianday(date('now')) - julianday(available_from) > 30
        AND julianday(date('now')) - julianday(dispatch_date) < 90
        GROUP BY client_order.product_id
        HAVING SUM(quantity) < 10
    """)
    return cur.fetchall()
