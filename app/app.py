from flask import Flask,render_template, request, jsonify,Blueprint
import route_planner
from views import views
# Example graph
'''
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
'''
#creates the app and redirects where to look for
def create_app():
    app = Flask(__name__,static_folder='static')
    app.register_blueprint(views,url_prefix="/")
    return app

app = create_app()

if __name__ == "__main__":
    app.run()

#run app here and go to http://localhost:5000/