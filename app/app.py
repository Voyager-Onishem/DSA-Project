from flask import Flask
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    return app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
    #rom waitress import serve
    #serve(app, host="0.0.0.0", port=8080)