#é, á, í, ó, ú, ñ ? ¿
from flask import Flask, request

app = Flask(__name__)

tasks = {}


# @app.route('/')
# def root():
#     return "method get /available (show all available tasks) \n \
#             method get /findTask?id= (show only one /findTask?id=) \n \
#             method post /addTask?id=&priority= (add new task using form) \n \
#             method delete /deleteTask?id= (delete new task) \n \
#             method put /updateTask?id= (update new task using json)"

# @app.route('/tasks', methods=['get'])
# def get_tasks():
#     return {
#         'ok': True,
#         'content': tasks,
#         'message': 'All tasks'
#     }

# @app.route('/addTask', methods=['post'])
# def add_task():
#     data = request.form
#     tasks[data['id']] = { 'priority': data['priority'] }
#     return 'ok', 201

# @app.route('/findTask', methods=['get'])
# def find_task():
#      return tasks[request.args.get('id')]

# @app.route('/deleteTask', methods=['delete'])
# def delete_task():
#     del tasks[request.args.get('id')]
#     return 'ok', 204

# @app.route('/updateTask', methods=['put'])
# def update_task():
#     tasks[request.args.get('id')].update(request.json)
#     return 'ok'


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


#
# apartments = {
#     'apt1' : {
#         'address': 'Elm Street 01'
#     },
#     'apt2': {
#         'address': 'Elm Street 18'
#     },
#     'apt3': {
#         'address': 'Acacia Avenue 22'
#     }
# }

# @app.route('/')
# def root():
#     return "method get /available"

# @app.route('/available', method=['get'])
# def get_apartments():
#     return {
#         'ok': True,
#         'content': apartments,
#         'message': 'All available apartments'
#     }



'''
from flask import Flask
from flask import request
from flask.templating import render_template
from flask.views import MethodView
from flask import send_file

from PIL import Image, ImageChops, ImageOps

import requests

app = Flask(__name__)
'''






# http://127.0.0.1:5000/image?src=https://ichef.bbci.co.uk/news/800/cpsprodpb/15665/production/_107435678_perro1.jpg&mirror=true&grayscale=true

'''
@app.route('/image')
def image():
    src = request.args.get("src")
    image_buffer = requests.get(src, stream=True).raw
    image = Image.open(image_buffer)

    mirror_flag = request.args.get('mirror')
    grayscale_flag = request.args.get('grayscale')

    new_image = image
    if mirror_flag == 'true':
        new_image = ImageOps.mirror(new_image)
    if grayscale_flag == 'true':
        new_image = new_image.convert('L')

    new_image.save('temp.jpg')
    return send_file('temp.jpg')
'''


'''
FLASK_APP=nombre_de_su_archivo.py FLASK_ENV=development flask run
'''

'''
@app.route('/user/<id>')
def get_user(id):
    return f"user: {id}"

@app.route('/name_post', methods=['POST'])
def name_post():
    json = request.json
    name = json["first_name"]
    return f"hello {name}"

@app.route('/name_form', methods=['POST'])
def name_form():
    data = request.form
    name = data['first_name']
    return f"hello {name}"


@app.route('/name')
def hello_world():
    first_name = request.args.get('first_name')
    return f"hello {first_name}"
'''

'''
contacts = {}


class Contact:
    def __init__(self, name, lastname, num_phone):
        self.name = name
        self.lastname = lastname
        self.num_phone = num_phone

    def show_info(self):
        return f"Name: {self.name} Lastname: {self.lastname} Phone:{self.num_phone}"

class PhoneDirectory(MethodView):
    def __init__(self, owner='unknown'):
        self.owner = owner
        # self.contacts = []

    def _find_contact(self, name, lastname):
        for idx, contact in enumerate(contacts):
            if contact.name== name and contact.lastname == lastname:
                return (True, idx)
        return (False, None)

    def get(self):
        id = request.args.get('id')
        return contacts[id]
        # name = request.args.get('name')
        # lastname = request.args.get('lastname')
        # exists, contact = self._find_contact(name, lastname)
        # if exists:
        #     return f"{contacts[contact].show_info()}"
        # else:
        #     return "doesnt exist"

    def post(self):

        data = request.form
        users[] = {
            'name': data['name'],
            'lastname': data['lastname],
            'num_phone': data['num_phone]
        }
        data = request.form
        contacts.append(Contact(data['name'], data['lastname'], data['num_phone']))
        print('len: ', len(contacts))
        return f"added contact {contacts[-1].show_info()}"

    def put(self):


def main():
    my_phone = PhoneDirectory()
    app = Flask(__name__)
    app.add_url_rule('/addContact', view_func=my_phone.as_view('addContact'), methods=['post'])
    app.add_url_rule('/findContact', view_func=my_phone.as_view('findContact'), methods=['get'])

    app.run()

if __name__ == '__main__':
    main()

'''

# departments = {
#     'dp1': {
#         'address': 'Elm street 01',
#     }
# }

# class DepartmentDirectory(MethodView):
#     def __init__(self, owner='unk'):
#         self.owner = owner

#     # @app.route('/showInfo', methods=['get'])
#     def show_info(self):
#         for name in departments:
#             return departments[name]['address']

# if __name__ == '__main__':
#     my_directory = DepartmentDirectory()
#     app.add_url_rule('/showInfo', view_func=my_directory.as_view('showInfo'), methods=['get'])
#     app.run()




#é, á, í, ó, ú, ñ ? ¿
'''
class Contact:
    def __init__(self, name, lastname, num_phone):
        self.name = name
        self.lastname = lastname
        self.num_phone = num_phone

class PhoneDirectory:
    def __init__(self, owner='unknown'):
        self.owner = owner
        self.contacts = []

    def add_contact(self, name, lastname, num_phone):
        self.contacts.append({
            'name': name,
            'lastname': lastname,
            'num_phone': num_phone
        })

    def find_contact(self, name, lastname, show=True):
        for idx, contact in enumerate(self.contacts):
            if contact['name'] == name and contact['lastname'] == lastname:
                if show:
                    print(contact)
                return idx
        print('doesnt exist')

    def del_contact(self, name, lastname):
        idx = self.find_contact(name, lastname, show=False)
        deleted_contact = self.contacts.pop(idx)
        print(deleted_contact)

    def show_contacts(self):
        for contact in self.contacts:
            print(contact)

    def modify_contact(self, name, lastname):
        idx = self.find_contact(name, lastname, show=False)
        self.contacts[idx] = {
            'name': input('name: '),
            'lastname': input('lastname: '),
            'num_phone': input('num_phone:' ),
        }
'''