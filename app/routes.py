# filepath: c:\Users\kippe\Documents\dev\slide-roulette\slide-roulette-game\app\routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from werkzeug.utils import secure_filename
from .forms import LoginForm, ImageForm, WordForm
from .models import Image, Word, Settings
from . import db
import os

main = Blueprint('main', __name__)  # Rename the Blueprint

@main.route('/')
def game():
    images = [{"url": image.url} for image in Image.query.all()]  # Serialize images
    words = [{"text": word.text} for word in Word.query.all()]  # Serialize words
    return render_template('game.html', images=images, words=words)

@main.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'admin_logged_in' not in session:
        return redirect(url_for('main.login'))

    image_form = ImageForm()
    word_form = WordForm()

    if request.method == 'POST':
        # Handle image upload
        if request.form.get('item_type') == 'image' and 'image' in request.files:
            image_file = request.files['image']
            if image_file.filename != '':
                filename = secure_filename(image_file.filename)
                upload_folder = current_app.config['UPLOAD_FOLDER']

                # Ensure the upload folder exists
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                image_path = os.path.join(upload_folder, filename)
                image_file.save(image_path)

                # Save image to the database
                new_image = Image(url=filename)
                db.session.add(new_image)
                db.session.commit()
                flash('Image uploaded and saved successfully!', 'success')

        # Handle word addition
        elif request.form.get('item_type') == 'word':
            word = request.form.get('word')
            if word:
                # Save word to the database
                new_word = Word(text=word)
                db.session.add(new_word)
                db.session.commit()

                # Save word to a text file
                word_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'words')
                if not os.path.exists(word_folder):
                    os.makedirs(word_folder)

                word_file_path = os.path.join(word_folder, 'words.txt')
                with open(word_file_path, 'a') as word_file:
                    word_file.write(f"{word}\n")

                flash('Word added and saved successfully!', 'success')

        # Redirect to avoid form resubmission
        return redirect(url_for('main.admin'))

    # Fetch current items for display
    images = Image.query.all()
    words = Word.query.all()
    return render_template('admin.html', image_form=image_form, word_form=word_form, images=images, words=words)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Form submitted:', form.password.data)  # Debugging line
        if form.password.data == 'password':  # Replace with your actual password
            session['admin_logged_in'] = True
            print('Admin logged in successfully.')
            return redirect(url_for('main.admin'))
        else:
            flash('Invalid password. Please try again.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/delete-image/<int:image_id>', methods=['POST'])
def delete_image(image_id):
    image = Image.query.get_or_404(image_id)
    image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.url)

    # Remove the image file from the filesystem
    if os.path.exists(image_path):
        os.remove(image_path)

    # Remove the image from the database
    db.session.delete(image)
    db.session.commit()
    flash('Image deleted successfully!', 'success')
    return redirect(url_for('main.admin'))


@main.route('/delete-word/<int:word_id>', methods=['POST'])
def delete_word(word_id):
    word = Word.query.get_or_404(word_id)

    # Remove the word from the database
    db.session.delete(word)
    db.session.commit()

    # Remove the word from the words.txt file
    word_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'words')
    word_file_path = os.path.join(word_folder, 'words.txt')
    if os.path.exists(word_file_path):
        with open(word_file_path, 'r') as file:
            lines = file.readlines()
        with open(word_file_path, 'w') as file:
            for line in lines:
                if line.strip() != word.text:
                    file.write(line)

    flash('Word deleted successfully!', 'success')
    return redirect(url_for('main.admin'))