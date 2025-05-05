import os
from app import create_app, db
from app.models import Image, Word

def populate_database():
    app = create_app()
    with app.app_context():
        upload_folder = app.config['UPLOAD_FOLDER']
        word_file_path = os.path.join(upload_folder, 'words', 'words.txt')

        # Populate images
        if os.path.exists(upload_folder):
            for filename in os.listdir(upload_folder):
                file_path = os.path.join(upload_folder, filename)
                if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
                    # Check if the image is already in the database
                    if not Image.query.filter_by(url=filename).first():
                        new_image = Image(url=filename)
                        db.session.add(new_image)
                        print(f"Added image: {filename}")

        # Populate words
        if os.path.exists(word_file_path):
            with open(word_file_path, 'r') as word_file:
                for line in word_file:
                    word = line.strip()
                    if word and not Word.query.filter_by(text=word).first():
                        new_word = Word(text=word)
                        db.session.add(new_word)
                        print(f"Added word: {word}")

        # Commit changes to the database
        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate_database()