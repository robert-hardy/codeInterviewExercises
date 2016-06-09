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
        CREATE TABLE orders
        (
            order_id NUMBER PRIMARY KEY,
            product_id NUMBER NOT NULL,
            quantity NUMBER NOT NULL,
            order_price NUMBER NOT NULL,
            dispatch_date DATE NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        );
    """)

def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

def initialize_db(filename):
    conn = sqlite.connect(filename, detect_types=sqlite.PARSE_DECLTYPES)
    conn.row_factory = dict_factory
    create_tables(conn)
    return conn
