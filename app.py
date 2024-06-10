# app.py
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
from cripto_scripts.encrypt_image import encrypt_image
from cripto_scripts.decrypt_image import decrypt_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'supersecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            input_image_path = os.path.join(
                app.config['UPLOAD_FOLDER'], filename)
            output_image_path = os.path.join(
                app.config['UPLOAD_FOLDER'], f'encrypted_{filename}.enc')
            key_path = os.path.join(
                app.config['UPLOAD_FOLDER'], f'key_{filename}.bin')

            file.save(input_image_path)
            encrypt_image(input_image_path, output_image_path, key_path)

            return render_template('index.html', encrypted_image=output_image_path, key_file=key_path)
    return render_template('index.html')


@app.route('/decrypt', methods=['POST'])
def decrypt():
    if 'encrypted_file' not in request.files or 'key_file' not in request.files:
        return redirect(request.url)
    encrypted_file = request.files['encrypted_file']
    key_file = request.files['key_file']
    if encrypted_file.filename == '' or key_file.filename == '':
        return redirect(request.url)
    if encrypted_file and key_file:
        encrypted_filename = secure_filename(encrypted_file.filename)
        key_filename = secure_filename(key_file.filename)
        encrypted_image_path = os.path.join(
            app.config['UPLOAD_FOLDER'], encrypted_filename)
        key_path = os.path.join(app.config['UPLOAD_FOLDER'], key_filename)
        output_image_path = os.path.join(
            app.config['UPLOAD_FOLDER'], f'decrypted_baidu.jpg')

        encrypted_file.save(encrypted_image_path)
        key_file.save(key_path)
        decrypt_image(encrypted_image_path, output_image_path, key_path)

        return render_template('index.html', decrypted_image=output_image_path)
    return redirect(request.url)


@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
