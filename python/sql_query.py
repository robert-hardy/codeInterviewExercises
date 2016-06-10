from datetime import date
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


def get_books_that_are_not_selling_well(conn, today_date=None):
    cur = conn.cursor()
    if today_date is None:
        today_date = date.today()
    query = """
        SELECT
            product_id,
            total_sold_in_last_year
        FROM (
            SELECT
                product.product_id,
                (CASE
                    WHEN
                        client_order.dispatch_date < date('{now}', '-1 years')
                        OR
                        client_order.dispatch_date IS NULL
                    THEN
                        0
                    ELSE
                        client_order.quantity
                END
                ) as total_sold_in_last_year,
                available_from
            FROM
                product LEFT OUTER JOIN client_order
                ON product.product_id = client_order.product_id
            WHERE
                available_from < date('{now}', '-1 months')
            ) AS a
        WHERE
            a.total_sold_in_last_year < 10
    """.format(now=today_date.isoformat())
    cur.execute(query)
    return cur.fetchall()
