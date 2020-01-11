import threading
import time
import numpy as np
from searching import main_sarch

class ExportingThread(threading.Thread):
    def __init__(self, problem_data):
        self.progress = 0
        self.output = {}
        self.status = 'created'
        self.problem_data = problem_data
        self.task_name = problem_data.name
        self.points = ''
        self.routes_plot = ''
        self.total_distance = ''
        self.total_load = ''
        self.sol_data = {}
        super().__init__()

    def run(self):

        self.status = 'Preparing data'
        self.progress = 25
        dist, demands, nun_of_vehicles, capacity, node_coords = self.prepare_data()
        time.sleep(0.1)

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


        # Your exporting stuff goes here ...
        # for _ in range(100):
        #     time.sleep(0.01)
        #     self.progress += 1

    def delay_start(self, sleep_time):
        time.sleep(sleep_time)
        self.run()

    @staticmethod
    def cal_euc_dist(x1, y1, x2, y2):
        return int(np.round(np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))))

    def prepare_data(self):

        demands = list(self.problem_data.demands.values())
        node_coords = list(self.problem_data.node_coords.values())
        size = len(node_coords)
        dist = np.zeros([size, size])
        for i in range(size):
            for j in range(size):
                dist[i][j] = self.cal_euc_dist(*node_coords[i], *node_coords[j])
        nun_of_vehicles = int(self.problem_data.name.split('k')[1])
        capacity = self.problem_data.capacity

        return dist, demands, nun_of_vehicles, capacity, node_coords

    def find_patch(self, dist, demands, nun_of_vehicles, capacity):
        routes, total_distance, total_load = main_sarch(dist, demands, nun_of_vehicles, capacity)
        self.total_distance = total_distance
        self.total_load = total_load
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
