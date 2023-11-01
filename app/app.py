from flask import Flask, render_template, request, jsonify,Blueprint
import route_planner

# Example graph
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

def create_app():
    app = Flask(__name__)

    @app.route('/index')
    def index():
        return render_template('index.html')
    '''
    @app.route('/route-planning-endpoint', methods=['POST'])
    def route_planning_endpoint():
        if request.json:
            start_station = request.json.get('start')
            end_station = request.json.get('end')
            # Calculate the route
            result = route_planner.dijkstra(metro_data, start_station, end_station)
            # Return the result as JSON
            return jsonify({"route": result})

        # Handle cases where the request doesn't have JSON data
        return jsonify({"error": "Invalid request"})
    '''
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
