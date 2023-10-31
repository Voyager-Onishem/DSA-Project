import heapq
from app import app
from flask import request, render_template, redirect, url_for
came_from={}
def dijkstra(graph, start, end):
    # Initialize distances with infinity for all stations except the start station.
    distances = {station: float('inf') for station in graph}
    distances[start] = 0
    
    # Priority queue to keep track of the stations to visit.
    queue = [(0, start)]

    while queue:
        current_distance, current_station = heapq.heappop(queue)

        # If the current station is the end station, we have found the shortest path.
        if current_station == end:
            path = []
            while current_station:
                path.append(current_station)
                current_station = graph[current_station]["previous"]
            return path[::-1]

        # Check all neighboring stations and update their distances if a shorter path is found.
        for neighbor, weight in graph[current_station]["neighbors"].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                graph[neighbor]["previous"] = current_station
                heapq.heappush(queue, (distance, neighbor))

def find_shortest_route(metro_data, start_station, end_station):
    graph = {}
    for station in metro_data["stations"]:
        station_name = station["name"]
        graph[station_name] = {"neighbors": {}, "previous": None}

    for connection in metro_data["connections"]:
        station1 = connection["station1"]
        station2 = connection["station2"]
        distance = connection["distance"]

        graph[station1]["neighbors"][station2] = distance
        graph[station2]["neighbors"][station1] = distance

    if start_station not in graph or end_station not in graph:
        return None

    route = dijkstra(graph, start_station, end_station)

    return route
def reconstruct_path(current_station):
    path = [current_station]
    while current_station in came_from:
        current_station = came_from[current_station]
        path.insert(0, current_station)
    return path
if __name__ == "__main__":
    # Sample usage
    metro_data = {
        "stations": [
            {"name": "Station A"},
            {"name": "Station B"},
            {"name": "Station C"}
        ],
        "connections": [
            {"station1": "Station A", "station2": "Station B", "distance": 2.5},
            {"station1": "Station B", "station2": "Station C", "distance": 3.0}
        ]
    }

    start_station = request.form['start_station']
    end_station = request.form['end_station']

    route = find_shortest_route(metro_data, start_station, end_station)
    print(f"Shortest Route from {start_station} to {end_station}: {route}")
