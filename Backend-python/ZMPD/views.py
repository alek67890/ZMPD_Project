import random
import json
import re

from model import ExportingThread
from flask import request

from app import app, exporting_threads


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
        data['data'][item]['firstSolution'] = str(exporting_threads[item].firstSolution)

    return json.dumps(data)


@app.route('/create', methods=['POST'])
def create():

    data = request.get_json()['data']
    alg = request.get_json()['alg']
    timeValue = int(request.get_json()['timeValue'])
    firstSolution = request.get_json()['firstSolution']

    capacity = re.search("^CAPACITY\s*:\s*(\d+)\s*$", data, re.MULTILINE).group(1)
    capacity = int(capacity)

    node_coords = re.findall(r"^(\d+)\s+([-+]?\d+\.*\d*)\s+([-+]?\d+\.*\d*)\s*$", data, re.MULTILINE)
    node_coords = {float(a): (float(b), float(c)) for a, b, c in node_coords}

    demands = re.findall(r"^(\d+)\s+(\d+)\s*$", data, re.MULTILINE)
    demands = {int(a): int(b) for a, b in demands}

    name = re.search("^NAME\s*:\s*(.+)*$", data, re.MULTILINE).group(1)

    depot = re.findall(r"^(\d+\.*\d*)\s+(\d+\.*\d*)\s*$", data, re.MULTILINE)
    depot = (float(depot[-1][0]), float(depot[-1][1]))

    problem_data = {'capacity': capacity, 'node_coords': node_coords, 'demands': demands, 'depot': depot}

    global exporting_threads

    thread_id = random.randint(0, 10000)
    exporting_threads[thread_id] = ExportingThread(problem_data, name, alg, firstSolution, timeValue)
    exporting_threads[thread_id].start()

    return 'task id: #%s' % thread_id


@app.route('/')
def home():

    return str('OK')