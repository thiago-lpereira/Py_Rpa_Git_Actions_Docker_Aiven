import unittest
from DolarCotacaoInsertPostgresPyinstall import DolarCotacaoInsertPostgresPyinstall

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = DolarCotacaoInsertPostgresPyinstall.test_client()

    def test_devops(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
 unittest.main()
