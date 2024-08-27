from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def server_info():
    return 'Server Is Accesible'

@app.route('/download/<filename>')
def download_file(filename):
    file_path = f'./{filename}'  # Ruta al fichero dentro de la carpeta 'files'
    try:
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
