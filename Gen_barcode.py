from flask import Flask, request, jsonify
import random, base64, io
import barcode
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/generate_barcode', methods=['POST'])
def generate_barcode():
    data = request.json
    data_code = data.get('data')

    # เช็คว่าข้อมูลไม่เกิน 8 ตัวอักษร
    if not data_code or len(data_code) > 8:
        return jsonify({
            "error": "Invalid input: 'data' is required and must be 8 characters or fewer."
        }), 400

    buf = io.BytesIO()
    bc = barcode.get('code39', data_code, writer=ImageWriter())
    bc.write(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()

    return jsonify({"barcodeCode": data_code, "imageBase64": b64})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
