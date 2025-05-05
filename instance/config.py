SECRET_KEY = 'your_secret_key_here'
ADMIN_PASSWORD = 'your_admin_password_here'
DATABASE_URI = 'sqlite:///site.db'  # Example for SQLite, modify as needed
UPLOAD_FOLDER = 'app/static/uploads'  # Folder for uploaded images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed image formats
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use SQLite as an example
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for performance