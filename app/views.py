from flask import Flask, render_template, request, jsonify, Blueprint
import os
import route_planner
from data_loader import metro_data
views=Blueprint("views","__name__")
@views.route("/")
def index():
    return render_template('index.html')
@views.route('/result')
def result():
    start_station = request.args.get('startStation')
    end_station = request.args.get('endStation')
    route_information = request.args.get('routeInformation')
    return render_template("result.html", startStation=start_station, endStation=end_station, routeInformation=route_information)

def payhav(start,end):
    return render_template("result.html",startStation=start,endStation=end)
@views.route('/route-planning-endpoint', methods=['POST'])
def route_planning_endpoint():
    if request.json:
        start_station = request.json.get('start')
        end_station = request.json.get('end')
        # Calculate the route
        result = route_planner.find_shortest_route(metro_data, start_station, end_station)
        # Return the result as JSON with the correct key
        return jsonify({"route": result})

    # Handle cases where the request doesn't have JSON data
    return jsonify({"error": "Invalid request"})
