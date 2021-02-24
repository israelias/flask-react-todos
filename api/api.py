import time
from flask import Flask

# deployment via Python directly
# yarn build then =>
# not encrypted.
app = Flask(__name__, static_folder='../build', static_url_path='/')

# localhost:5000
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
