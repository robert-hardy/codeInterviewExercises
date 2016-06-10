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
        (1003, 104, 5, 94, "2016-01-01"),
        (1004, 105, 11, 95, "2014-06-01"),
        (1005, 103, 1,  92, "2016-05-01"),
        (1007, 104, 6,  92, "2016-05-01")
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
            {'product_id': 103, 'total_orders_in_last_year': 2},
            {'product_id': 104, 'total_orders_in_last_year': 6},
            {'product_id': 105, 'total_orders_in_last_year': 0}
        ])


class TestQueryBeforeGroupBy(unittest.TestCase):
    # Checks that we can produce a list, for each not-new book
    # of the sizes of orders in the last year.
    # These results will be grouped in the main query.
    def execute_query(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT
                name,
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
                ) as order_size_in_last_year
            FROM
                product LEFT OUTER JOIN client_order
                ON product.product_id = client_order.product_id
            WHERE
                available_from < date('{now}', '-1 months');
        """.format(now=self.today.isoformat()))
        results = [ (r['name'], r['order_size_in_last_year']) for r in cur.fetchall() ]
        return results

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

    def test_no_orders_at_all(self):
        # Basically gives us a list of the not-new books
        results = self.execute_query()
        self.assertEqual(results, [
            (u'book3', 0),
            (u'book4', 0),
            (u'book5', 0)
        ])

    def test_one_new_book_with_one_order(self):
        order_rows = [
            (1000, 101, 1,  91, "2016-04-01")
        ]
        populate_order_table(self.conn, order_rows)
        results = self.execute_query()
        self.assertEqual(results, [
            (u'book3', 0),
            (u'book4', 0),
            (u'book5', 0)
        ])

    def test_one_not_new_book_with_one_order(self):
        order_rows = [
            (1000, 103, 1,  91, "2016-04-01")
        ]
        populate_order_table(self.conn, order_rows)
        results = self.execute_query()
        self.assertEqual(results, [
            (u'book3', 1),
            (u'book4', 0),
            (u'book5', 0)
        ])

    def test_with_two_good_orders_for_book3(self):
        order_rows = [
            (1000, 101, 1,  91, "2016-04-01"),
            (1001, 103, 1,  92, "2016-05-01"),
            (1002, 101, 10, 93, "2015-05-01"),
            (1003, 104, 11, 94, "2016-01-01"),
            (1004, 105, 11, 95, "2014-06-01"),
            (1005, 103, 1,  92, "2016-05-01")
        ]
        populate_order_table(self.conn, order_rows)
        results = self.execute_query()
        self.assertEqual(results, [
            (u'book3', 1),
            (u'book3', 1),
            (u'book4', 11),
            (u'book5', 0)
        ])

    def test_using_orders_in_test_on_main_query(self):
        full_populate_tables(self.conn)
        results = self.execute_query()
        self.assertEqual(results, [
            (u'book3', 1),
            (u'book3', 1),
            (u'book4', 5),
            (u'book4', 6),
            (u'book5', 0)
        ])
