from flask import Flask, request, jsonify
import base64, io
import barcode
from barcode.writer import ImageWriter
from barcode.codex import Code39  # Import class Code39 โดยตรง

app = Flask(__name__)

@app.route('/generate_barcode', methods=['POST'])
def generate_barcode():
    data = request.json
    data_code = data.get('data')

    if not data_code:
        return jsonify({'error': 'Missing data in request'}), 400

    try:
        buf = io.BytesIO()
        # สร้าง barcode Code39 โดยปิด checksum
        bc = Code39(data_code, writer=ImageWriter(), add_checksum=False)
        bc.write(buf)

        # แปลงรูปภาพเป็น base64
        b64 = base64.b64encode(buf.getvalue()).decode()

        return jsonify({"barcodeCode": data_code, "imageBase64": b64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
