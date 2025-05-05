# filepath: c:\Users\kippe\Documents\dev\slide-roulette\slide-roulette-game\init_db.py
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Create all tables
    print("Database initialized successfully!")