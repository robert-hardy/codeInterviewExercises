import unittest

from datetime import date
from sql_query import initialize_db

class TestDBInitialize(unittest.TestCase):
    def test_tables_exist(self):
        conn = initialize_db(':memory:')
        cur = conn.cursor()
        cur.execute("""
            SELECT name FROM sqlite_master WHERE type='table';
        """)
        result = cur.fetchall()
        table_names = set([ r['name'] for r in result ])
        self.assertEqual(table_names,
            set(['product', 'client_order'])
        )

    def test_product_table(self):
        conn = initialize_db(':memory:')
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM product;
        """)
        result = cur.fetchall()
        product_names = set([ r['name'] for r in result ])
        product_dates = set([ r['available_from'] for r in result ])
        self.assertEqual(product_names,
            set(['book1', 'book2', 'book3', 'book4', 'book5'])
        )
        self.assertEqual(product_dates,
            set([
                date(2016, 6, 1),
                date(2017, 6, 1),
                date(2016, 3, 1),
                date(2014, 6, 1),
                date(2015, 6, 1)
            ])
        )

    def test_order_table(self):
        conn = initialize_db(':memory:')
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM client_order;
        """)
        result = cur.fetchall()
        quantity = set([ r['quantity'] for r in result ])
        self.assertEqual(quantity,
            set([1, 1, 10, 11, 11])
        )
