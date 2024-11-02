from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if url:
        # Generate QR code
        qr = qrcode.make(url)
        # Save the QR code to an in-memory file
        img_io = io.BytesIO()
        qr.save(img_io, 'PNG')
        img_io.seek(0)
        # Send the file as a download
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    else:
        return "No URL provided", 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)

