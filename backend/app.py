from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import api_routes
from waitress import serve
import os

# Load environment variables
load_dotenv()

# Setup Flask app
app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(api_routes, url_prefix='/api')

# If the script is run directly, use Waitress to serve the app
if __name__ == "__main__":
    # Get the port from the environment variable (Render will assign a port dynamically)
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)  # Serve on all interfaces and dynamic port
