import tsplib95
import random
import json
import re

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
        data['data'][item]['points'] = str(exporting_threads[item].points)
        data['data'][item]['routes_plot'] = str(exporting_threads[item].routes_plot)
        data['data'][item]['total_distance'] = str(exporting_threads[item].total_distance)
        data['data'][item]['total_load'] = str(exporting_threads[item].total_load)
        data['data'][item]['alg'] = str(exporting_threads[item].alg_type)

    return json.dumps(data)
@app.route('/create', methods=['POST'])
def create():
    # print(request.headers)
    # print(request.data)
    data = request.get_json()['data']
    alg = request.get_json()['alg']
    timeValue = int(request.get_json()['timeValue'])
    # print(data)
    problem_data = tsplib95.utils.load_problem_fromstring(data)

    problem_data2 = tsplib95.utils.load_problem_fromstring(data)

    capacity = re.search("^CAPACITY\s*:\s*(\d+)\s*$", data, re.MULTILINE).group(1)
    capacity = int(capacity)

    node_coords = re.findall(r"^(\d+)\s+([-+]?\d+\.*\d*)\s+([-+]?\d+\.*\d*)\s*$", data, re.MULTILINE)
    node_coords = {float(a): (float(b), float(c)) for a, b, c in node_coords}

    demands = re.findall(r"^(\d+)\s+(\d+)\s*$", data, re.MULTILINE)
    demands = {int(a): int(b) for a, b in demands}

    name = re.search("^NAME\s*:\s*(.+)*$", data, re.MULTILINE).group(1)
    name

    problem_data2 = {'capacity': capacity, 'node_coords': node_coords, 'demands': demands}
    # data = data.split("\n")
    # sort_data = {}
    # key = ""
    # for index, item in enumerate(data):
    #     if (item.find(":") != -1):
    #         print(item)
    #         temp = item.split(":")
    #         sort_data[temp[0].lower()] = temp[1]
    #     else:
    #         if (item.find(" ") == -1):
    #             key = item.lower()
    #         else:
    #             temp = item.split(" ")
    #             try:
    #                 sort_data[key][temp[0]] = list(map(float, list(temp[1:])))
    #             except:
    #                 sort_data[key] = {}
    #                 sort_data[key][temp[0]] = list(map(float, list(temp[1:])))

    global exporting_threads

    # thread_id = random.randint(0, 10000)
    # exporting_threads[thread_id] = ExportingThread(problem_data,problem_data.name, alg, timeValue)
    # exporting_threads[thread_id].delay_start(0.1)

    thread_id2 = random.randint(0, 10000)
    exporting_threads[thread_id2] = ExportingThread(problem_data2, problem_data.name, alg, timeValue, True)
    exporting_threads[thread_id2].delay_start(0.1)

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

