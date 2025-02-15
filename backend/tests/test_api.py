import unittest
from app import create_app

class TestGenerateQRCodeAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_generate_qr_success(self):
        response = self.client.post('/generate', json={'url': 'https://example.com'})
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('qr_code', data)

    def test_generate_qr_invalid_url(self):
        response = self.client.post('/generate', json={'url': 'invalid-url'})
        data = response.get_json()
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid or missing URL")

    def test_generate_qr_missing_url(self):
        response = self.client.post('/generate', json={})
        data = response.get_json()
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid or missing URL")

    def test_generate_qr_invalid_json(self):
        response = self.client.post('/generate', data="invalid json", content_type='application/json')
        data = response.get_json()
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid JSON format or missing fields.")
