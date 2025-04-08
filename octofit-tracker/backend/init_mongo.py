from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")

# Initialize the database
db = client["octofit_db"]

# Create collections
collections = ["users", "teams", "activity", "leaderboard", "workouts"]
for collection in collections:
    db.create_collection(collection, capped=False, size=None, max=None)

# Ensure unique index for the users collection
db["users"].create_index("email", unique=True)

print("Database and collections initialized successfully.")
