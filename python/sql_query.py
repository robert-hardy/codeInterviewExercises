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

def populate_product_table(conn):
    rows = [
        (101, "book1", 91, "2016-06-01"),
        (102, "book2", 92, "2017-06-01"),
        (103, "book3", 93, "2016-03-01"),
        (104, "book4", 94, "2014-06-01"),
        (105, "book5", 95, "2015-06-01")
    ]
    cur = conn.cursor()
    query = """
        INSERT OR IGNORE INTO product
        VALUES (?, ?, ?, ?)
    """
    try:
        cur.executemany(query, rows)
        conn.commit()
    except:
        raise

def populate_order_table(conn):
    rows = [
        (1000, 101, 1,  91, "2016-06-01"),
        (1001, 103, 1,  92, "2017-06-01"),
        (1002, 101, 10, 93, "2016-03-01"),
        (1003, 104, 11, 94, "2014-06-01"),
        (1004, 105, 11, 95, "2015-06-01")
    ]
    cur = conn.cursor()
    query = """
        INSERT OR IGNORE INTO client_order
        VALUES (?, ?, ?, ?, ?)
    """
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
    conn = sqlite.connect(filename, detect_types=sqlite.PARSE_DECLTYPES)
    conn.row_factory = dict_factory
    create_tables(conn)
    populate_product_table(conn)
    populate_order_table(conn)
    return conn
