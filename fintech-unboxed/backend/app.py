from flask import Flask
from pymongo import MongoClient
from config.settings import MONGO_URI
from routes.api import api_bp

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.financial_data

# Register API routes
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return "Welcome to FinTech Unboxed!"

if __name__ == '__main__':
    app.run(debug=True)