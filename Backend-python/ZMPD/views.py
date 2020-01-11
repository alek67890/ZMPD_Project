import tsplib95
import random
import json
from model import ExportingThread
from flask import request
from flask import jsonify

from flask import Flask

from app import app, exporting_threads

# class ExportingThread(threading.Thread):
#     def __init__(self):
#         self.progress = 0
#         self.output = {}
#         super().__init__()
#
#     def run(self):
#         # Your exporting stuff goes here ...
#         for _ in range(100):
#             time.sleep(1)
#             self.progress += 1
#
#         self.output['final'] = "dsadasd"
#

@app.route('/tasks')
def index():
    global exporting_threads

    name = list(exporting_threads.keys())

    data = {}
    data['keys'] = name
    data['data'] = {}


    for item in name:
        data['data'][item] = {}
        data['data'][item]['name'] = str(exporting_threads[item].task_name)
        data['data'][item]['progress'] = str(exporting_threads[item].progress)
        data['data'][item]['output'] = str(exporting_threads[item].output)
        data['data'][item]['status'] = str(exporting_threads[item].status)

    return json.dumps(data)
@app.route('/create', methods=['POST'])
def create():
    # print(request.headers)
    # print(request.data)
    data = request.get_json()['data']
    # print(data)
    problem_data = tsplib95.utils.load_problem_fromstring(data)
    data = data.split("\n")
    sort_data = {}
    key = ""
    for index, item in enumerate(data):
        if (item.find(":") != -1):
            print(item)
            temp = item.split(":")
            sort_data[temp[0].lower()] = temp[1]
        else:
            if (item.find(" ") == -1):
                key = item.lower()
            else:
                temp = item.split(" ")
                try:
                    sort_data[key][temp[0]] = list(map(float, list(temp[1:])))
                except:
                    sort_data[key] = {}
                    sort_data[key][temp[0]] = list(map(float, list(temp[1:])))

    global exporting_threads

    thread_id = random.randint(0, 10000)
    exporting_threads[thread_id] = ExportingThread(problem_data.name)
    exporting_threads[thread_id].delay_start(10)
    # exporting_threads[thread_id].start()

    return 'task id: #%s' % thread_id


@app.route('/task/<int:thread_id>')
def progress(thread_id):
    global exporting_threads

    return str(exporting_threads[thread_id].progress)



@app.route('/output/<int:thread_id>')
def output(thread_id):
    global exporting_threads

    return str(exporting_threads[thread_id].output)

