import qrcode
import io
import base64

def generate_qr_code(url):
    qr = qrcode.make(url)
    buffered = io.BytesIO()

    # Save qr image into memory buffer
    qr.save(buffered, format="PNG")
    
    # Encode the image into a base64 string
    return base64.b64encode(buffered.getvalue()).decode()