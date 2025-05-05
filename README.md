# Slide Roulette Game

## Overview
The Slide Roulette Game is a web application built with Flask that allows users to play a fun and interactive slide roulette game. The application includes an admin panel for managing game content, such as images and words, and requires authentication for administrative actions.

## Features
- User-friendly game interface
- Admin panel for content management
- Secure login for administrators
- Ability to add and modify images and words

## Project Structure
```
slide-roulette-game
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── game.html
│   │   ├── admin.html
│   │   └── login.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── instance
│   └── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd slide-roulette-game
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration
- Update the `instance/config.py` file with your desired settings, including the secret key and database configurations.

## Running the Application
To start the application, run:
```
python run.py
```
The application will be accessible at `http://127.0.0.1:5000`.

## Usage
- Navigate to the game page to play the slide roulette game.
- Access the admin page by logging in with the administrator password to manage images and words.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.