from flask import Flask, request, jsonify
import random, base64, io
import barcode
from barcode.writer import ImageWriter

app = Flask(__name__)

@app.route('/generate_barcode', methods=['POST'])
def generate_barcode():
    data = request.json
    data_code = data.get('data')

    
    
    buf = io.BytesIO()
    bc = barcode.get('code39', data_code, writer=ImageWriter())
    bc.write(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    
    return jsonify({"barcodeCode": data_code, "imageBase64": b64})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)