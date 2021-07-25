#é, á, í, ó, ú, ñ ? ¿
from flask import Flask, request

app = Flask(__name__)

apartments = {
    'apt1' : {
        'address': 'Elm Street 01'
    },
    'apt2': {
        'address': 'Elm Street 18'
    },
    'apt3': {
        'address': 'Acacia Avenue 22'
    }
}

@app.route('/')
def root():
    return "method get /available"

@app.route('/available', method=['get'])
def get_apartments():
    return {
        'ok': True,
        'content': apartments,
        'message': 'All available apartments'
    }

if __name__ == '__main__':
    app.run()
