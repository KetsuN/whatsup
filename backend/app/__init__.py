from flask import Flask
import redis


# Initialize the app
app = Flask(__name__)
app.config.from_pyfile("config.py")

if not app.config.get("API_KEY"):
    raise SystemExit("API_KEY was not found.")

# INitialize redis
redis_db = redis.Redis.from_url(url=app.config.get("REDIS_URL"))

from app import views
