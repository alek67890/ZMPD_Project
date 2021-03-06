# from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model(dist, demands, K, capacity):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = dist
    data['demands'] = demands
    data['vehicle_capacities'] = K * [capacity]
    data['num_vehicles'] = K
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, assignment):
    """Prints assignment on console."""
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))
    return total_distance, total_load


def main_sarch(dist, demands, K, capacity, alg_type, firstSolution, time_limit=360):

    data = create_data_model(dist, demands, K, capacity)

    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()

    if alg_type == 'AUTOMATIC':
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC)

    if alg_type == "GREEDY_DESCENT":
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.GREEDY_DESCENT)

    elif alg_type == "GUIDED_LOCAL_SEARCH":
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)

    elif alg_type == "SIMULATED_ANNEALING":
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.SIMULATED_ANNEALING)

    elif alg_type == "TABU_SEARCH":
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.TABU_SEARCH)

    elif alg_type == "OBJECTIVE_TABU_SEARCH":
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.OBJECTIVE_TABU_SEARCH)

    search_parameters.time_limit.seconds = time_limit

    if firstSolution == "PATH_MOST_CONSTRAINED_ARC":
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_MOST_CONSTRAINED_ARC)

    elif firstSolution == "CHRISTOFIDES":
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.CHRISTOFIDES)

    else:
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.AUTOMATIC)

    assignment = routing.SolveWithParameters(search_parameters)

    def get_routes(manager, routing, solution, num_routes):
        routes = []
        for route_nbr in range(num_routes):
            index = routing.Start(route_nbr)
            route = [manager.IndexToNode(index)]
            while not routing.IsEnd(index):
                index = solution.Value(routing.NextVar(index))
                route.append(manager.IndexToNode(index))
            routes.append(route)
        return routes

    # Print solution on console.
    if assignment:
        total_distance, total_load = print_solution(data, manager, routing, assignment)
        routes = get_routes(manager, routing, assignment, data['num_vehicles'])
        for i, route in enumerate(routes):
            print('Route', i, route)
    else:
        routes = []
        total_distance, total_load = 0, 0

    return routes, total_distance, total_load
