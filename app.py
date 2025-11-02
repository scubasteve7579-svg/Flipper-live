from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/amazon')
def amazon():
    return send_from_directory('.', 'amazon.html')

@app.route('/health')
def health():
    return jsonify(status="ok", app="Flipper LIVE", url="flipper.website")

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
