#é, á, í, ó, ú, ñ ? ¿
from flask import Flask, request

app = Flask(__name__)

apartments = {}

@app.route('/')
def root():
    return "method get /available  (show all available apartments) \n \
            method get /findApartment?id= (show only one /findApartment?id=) \n \
            method post /addApartment?id=&address= (add new apartment using form)"

@app.route('/addApartment', methods=['post'])
def add_apartment():
    data = request.form
    apartments[data['id']] = { 'address': data['address'] }
    return 'ok', 201

@app.route('/findApartment', methods=['get'])
def find_apartment():
     return apartments[request.args.get('id')]

@app.route('/available', methods=['get'])
def get_apartments():
    return {
        'ok': True,
        'content': apartments,
        'message': 'All available apartments'
    }

if __name__ == '__main__':
    app.run()