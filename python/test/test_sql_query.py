import unittest

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
            set(['product', 'orders'])
        )

    def test_product_table(self):
        conn = initialize_db(':memory:')
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM product;
        """)
        result = cur.fetchall()
        product_names = set([ r['name'] for r in result ])
        self.assertEqual(product_names,
            set(['book1', 'book2', 'book3', 'book4', 'book5'])
        )
