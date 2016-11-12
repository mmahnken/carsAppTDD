import unittest
from server import app

class CarsIntegrationTest(unittest.TestCase):
    def setUp(self):
        """Gets called before every test."""

        self.client = app.test_client()


    def test_index_render(self):

        result = self.client.get('/')
        some_html = result.data

        self.assertIn("cars app", some_html)

    def test_chart_render(self):
        result = self.client.get('/charts')
        some_html = result.data

        self.assertIn("<h1>Brands Counts</h1>", some_html)
        self.assertIn("<canvas", some_html)



    

if __name__ == "__main__":
    unittest.main()