from flask import Flask
from whitenoise import WhiteNoise
import os
from leaf_analysis import analyze_leaf

app = Flask(__name__, static_folder='static')
app.wsgi_app = WhiteNoise(app.wsgi_app, root=app.static_folder)  # This line is the key
app.config['WHITENOISE_AUTOREFRESH'] = True  # Optional, but helpful for development
app.config['WHITENOISE_USE_FINDERS'] = True  # Optional

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # ... (your upload route code)

if __name__ == '__main__':
    app.run(debug=True)