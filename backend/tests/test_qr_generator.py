import unittest
import base64
import qrcode
import io
from app.qr_generator import generate_qr_code  # Replace 'your_module' with the actual module name

class TestGenerateQRCode(unittest.TestCase):
    def test_qr_code_generation(self):
        url = "https://example.com"
        qr_base64 = generate_qr_code(url)
        
        # Decode the base64 string back to image bytes
        qr_bytes = base64.b64decode(qr_base64)
        
        
        # Open the image and verify it's a valid QR code
        qr = qrcode.make(url)
        expected_io = io.BytesIO()
        qr.save(expected_io, 'PNG')
        expected_bytes = expected_io.getvalue()
        
        self.assertEqual(qr_bytes, expected_bytes)