import unittest

from datetime import date

from sql_query import (
    initialize_db,
    populate_product_table,
    populate_order_table
)

def populate_tables(conn):
    product_rows = [
        (101, "book1", 91, "2016-05-15"),
        (102, "book2", 92, "2017-06-01"),
        (103, "book3", 93, "2016-03-01"),
        (104, "book4", 94, "2014-06-01"),
        (105, "book5", 95, "2015-06-01")
    ]
    order_rows = [
        (1000, 101, 1,  91, "2016-04-01"),
        (1001, 103, 1,  92, "2016-05-01"),
        (1002, 101, 10, 93, "2015-05-01"),
        (1003, 104, 11, 94, "2016-01-01"),
        (1004, 105, 11, 95, "2014-06-01")
    ]
    populate_product_table(conn, product_rows)
    populate_order_table(conn, order_rows)

class TestDBInitialize(unittest.TestCase):
    def setUp(self):
        self.conn = initialize_db(':memory:')
        populate_tables(self.conn)
        self.cur = self.conn.cursor()

    def test_tables_exist(self):
        self.cur.execute("""
            SELECT name FROM sqlite_master WHERE type='table';
        """)
        results = self.cur.fetchall()
        table_names = set([ r['name'] for r in results ])
        self.assertEqual(table_names,
            set(['product', 'client_order'])
        )

    def test_product_table(self):
        self.cur.execute("""
            SELECT * FROM product;
        """)
        results = self.cur.fetchall()
        product_names = set([ r['name'] for r in results ])
        product_dates = set([ r['available_from'] for r in results ])
        self.assertEqual(product_names,
            set(['book1', 'book2', 'book3', 'book4', 'book5'])
        )
        self.assertEqual(product_dates,
            set([
                date(2016, 5, 15),
                date(2017, 6, 1),
                date(2016, 3, 1),
                date(2014, 6, 1),
                date(2015, 6, 1)
            ])
        )

    def test_order_table(self):
        self.cur.execute("""
            SELECT * FROM client_order;
        """)
        results = self.cur.fetchall()
        quantity = set([ r['quantity'] for r in results ])
        self.assertEqual(quantity,
            set([1, 1, 10, 11, 11])
        )

class TestGroupBy(unittest.TestCase):
    def setUp(self):
        self.conn = initialize_db(':memory:')
        populate_tables(self.conn)
        self.cur = self.conn.cursor()

    def test(self):
        self.cur.execute("""
            SELECT client_order.product_id, SUM(quantity) as total_sold
            FROM
                client_order JOIN product
                ON client_order.product_id = product.product_id
            WHERE julianday(date('now')) - julianday(available_from) > 30
            AND julianday(date('now')) - julianday(dispatch_date) < 90
            GROUP BY client_order.product_id
            HAVING SUM(quantity) < 10
        """)
        results = self.cur.fetchall()
        products = [ r['product_id'] for r in results ]
        self.assertEqual(products, [103])

    def test_books_older_than_1_month(self):
        self.cur.execute("""
            SELECT *
            FROM product
            WHERE julianday(date('now')) - julianday(available_from) > 30
        """)
        results = self.cur.fetchall()
        self.assertNotEqual(results, [])
