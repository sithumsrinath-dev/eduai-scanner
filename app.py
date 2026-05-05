import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# EduAI Scanner configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    # පද්ධතියේ ප්‍රධාන ක්‍රියාකාරීත්වය මෙතැනින් පටන් ගනී
    return jsonify({'message': 'Scan successful! Testing EduAI connection...'})

if __name__ == '__main__':
    app.run(debug=True)
