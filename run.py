from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    tz = timezone('America/New_York')
    return "Current time: " + datetime.now(tz).strftime('%m-%d-%Y %H:%M:%S')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)