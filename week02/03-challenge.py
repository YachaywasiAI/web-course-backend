#é, á, í, ó, ú, ñ ? ¿
from flask import Flask, request

app = Flask(__name__)

tasks = {}

@app.route('/')
def root():
    return "method get /available (show all available tasks) \n \
            method get /findTask?id= (show only one /findTask?id=) \n \
            method post /addTask?id=&priority= (add new task using form) \n \
            method delete /deleteTask?id= (delete new task) \n \
            method put /updateTask?id= (update new task using json)"

@app.route('/tasks', methods=['get'])
def get_tasks():
    return {
        'ok': True,
        'content': tasks,
        'message': 'All tasks'
    }

@app.route('/addTask', methods=['post'])
def add_task():
    data = request.form
    tasks[data['id']] = { 'priority': data['priority'] }
    return 'ok', 201

@app.route('/findTask', methods=['get'])
def find_task():
     return tasks[request.args.get('id')]

@app.route('/deleteTask', methods=['delete'])
def delete_task():
    del tasks[request.args.get('id')]
    return 'ok', 204

@app.route('/updateTask', methods=['put'])
def update_task():
    tasks[request.args.get('id')].update(request.json)
    return 'ok'

if __name__ == '__main__':
    app.run()