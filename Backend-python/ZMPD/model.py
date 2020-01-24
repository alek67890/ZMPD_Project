import threading
import time
import numpy as np
from searching import main_sarch


class ExportingThread(threading.Thread):
    def __init__(self, problem_data, name, alg_type, firstSolution, timeValue):
        self.progress = 0
        self.output = {}
        self.status = 'created'
        self.problem_data = problem_data
        self.task_name = name
        self.points = ''
        self.routes_plot = ''
        self.total_distance = ''
        self.total_load = ''
        self.sol_data = {}
        self.alg_type = alg_type
        self.timeValue = timeValue
        self.firstSolution = firstSolution
        super().__init__()

    def run(self):

        self.status = 'Preparing data'
        self.progress = 25

        dist, demands, nun_of_vehicles, capacity, node_coords = self.prepare_data()

        self.status = 'Finding patch'
        self.progress = 50
        routes = self.find_patch(dist, demands, nun_of_vehicles, capacity)
        time.sleep(0.1)

        self.status = 'Preparing output'
        self.progress = 90
        self.prepare_output(node_coords, routes)
        self.progress = 100
        time.sleep(0.1)

        self.output['final'] = "dsadasd"
        self.status = 'finished'

    @staticmethod
    def cal_euc_dist(x1, y1, x2, y2):
        return np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        # return int(np.round(np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))))

    def prepare_data(self):
        # print(self.problem_data)
        depot = self.problem_data['depot']
        demands = self.problem_data['demands']
        node_coords = list(self.problem_data['node_coords'].values())
        size = len(node_coords)

        if float(list(demands)[-1]) == depot[0] and float(list(demands.values())[-1]) == depot[1]:
            demands = list(demands.values())
        else:
            node_coords.append(depot)
            demands = list(demands.values())
            demands.append(0)
            size = len(node_coords)

            node_coords[0], node_coords[-1] = node_coords[-1], node_coords[0]
            demands[0], demands[-1] = demands[-1], demands[0]

        dist = np.zeros([size, size])
        for i in range(size):
            for j in range(size):
                dist[i][j] = self.cal_euc_dist(*node_coords[i], *node_coords[j])

        capacity = self.problem_data['capacity']
        num_of_vehicles = int(np.ceil(np.sum(demands) / capacity))

        return dist, demands, num_of_vehicles, capacity, node_coords

    def find_patch(self, dist, demands, nun_of_vehicles, capacity):

        try:
            routes, total_distance, total_load = main_sarch(dist, demands, nun_of_vehicles, capacity, self.alg_type, self.firstSolution, self.timeValue, )
            self.total_distance = total_distance
            self.total_load = total_load
        except:
            print('error')
        return routes

    def prepare_output(self, node_coords, routes):
        x = []
        y = []
        for item in node_coords:
            x.append(item[0])
            y.append(item[1])
        points = [x, y]
        routes_plot = []
        for route in routes:
            print(route)
            xx = []
            yy = []
            for place in route:
                xx.append(node_coords[place][0])
                yy.append(node_coords[place][1])
            routes_plot.append([xx, yy])

        self.points = points
        self.routes_plot = routes_plot
