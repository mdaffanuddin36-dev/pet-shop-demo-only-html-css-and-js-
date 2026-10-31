from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    return "index.html not found", 440

@app.route('/health')
def health():
    return {"status": "ok", "message": "Poket Vet Demo API / Server is running"}

# For Vercel Serverless Function compatibility
app_instance = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)