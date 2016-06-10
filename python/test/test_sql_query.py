import unittest

from datetime import date

from sql_query import (
    initialize_db,
    populate_product_table,
    populate_order_table,
    get_books_that_are_not_selling_well
)

class TestDBInitialize(unittest.TestCase):
    def setUp(self):
        self.conn = initialize_db(':memory:')
        product_rows = [
            (101, "book1", 91, "2016-05-15"),
            (102, "book2", 92, "2017-06-01")
        ]
        order_rows = [
            (1000, 101, 1,  91, "2016-04-01"),
            (1001, 103, 1,  92, "2016-05-01")
        ]
        populate_product_table(self.conn, product_rows)
        populate_order_table(self.conn, order_rows)

    def test_product_table(self):
        cur = self.conn.cursor()
        cur.execute("SELECT name FROM product;")
        product_names = set([ r['name'] for r in cur.fetchall() ])
        self.assertEqual(product_names, set(['book1', 'book2']))

    def test_order_table(self):
        cur = self.conn.cursor()
        cur.execute("SELECT quantity FROM client_order;")
        quantity = set([ r['quantity'] for r in cur.fetchall() ])
        self.assertEqual(quantity, set([1, 1]))


def full_populate_tables(conn):
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


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.today = date(2016, 6, 10)

    def test(self):
        conn = initialize_db(':memory:')
        full_populate_tables(conn)
        results = get_books_that_are_not_selling_well(conn, self.today)
        self.assertEqual(results, [
            {'product_id': 103, 'total_sold_in_last_year': 1},
            {'product_id': 105, 'total_sold_in_last_year': 0}
        ])


class TestNoOrders(unittest.TestCase):
    def setUp(self):
        self.conn = initialize_db(':memory:')
        product_rows = [
            (101, "book1", 91, "2016-05-15"),
            (102, "book2", 92, "2017-06-01"),
            (103, "book3", 93, "2016-03-01"),
            (104, "book4", 94, "2014-06-01"),
            (105, "book5", 95, "2015-06-01")
        ]
        populate_product_table(self.conn, product_rows)
        self.today = date(2016, 6, 10)

    def test_outer_join(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT
                *
            FROM
                product LEFT OUTER JOIN client_order
                ON product.product_id = client_order.product_id;
        """)
        results = [ (r['name'], r['quantity']) for r in cur.fetchall() ]
        self.maxDiff = 2000
        self.assertEqual(results, [
            (u'book1', None),
            (u'book2', None),
            (u'book3', None),
            (u'book4', None),
            (u'book5', None)
        ])

class TestOneBookWithOneOrder(unittest.TestCase):
    def setUp(self):
        self.conn = initialize_db(':memory:')
        product_rows = [
            (101, "book1", 91, "2016-05-15"),
            (102, "book2", 92, "2017-06-01"),
            (103, "book3", 93, "2016-03-01"),
            (104, "book4", 94, "2014-06-01"),
            (105, "book5", 95, "2015-06-01")
        ]
        order_rows = [
            (1000, 101, 1,  91, "2016-04-01")
        ]
        populate_product_table(self.conn, product_rows)
        populate_order_table(self.conn, order_rows)
        self.today = date(2016, 6, 10)

    def test_outer_join(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT
                *
            FROM
                product LEFT OUTER JOIN client_order
                ON product.product_id = client_order.product_id;
        """)
        results = [ (r['name'], r['quantity']) for r in cur.fetchall() ]
        self.maxDiff = 2000
        self.assertEqual(results, [
            (u'book1', 1),
            (u'book2', None),
            (u'book3', None),
            (u'book4', None),
            (u'book5', None)
        ])
