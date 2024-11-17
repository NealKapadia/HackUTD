from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import api_routes
from asgiref.wsgi import WsgiToAsgi

# Load environment variables
load_dotenv()

# Setup Flask app
app = Flask(__name__)
CORS(app)

app.register_blueprint(api_routes, url_prefix='/api')
asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run(debug=True)
