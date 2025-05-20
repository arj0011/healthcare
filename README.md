Healthcare Management System
A modular, scalable Flask web application built using the Flask Factory Pattern. This project leverages Flask extensions and best practices for building robust web apps, including user authentication, image upload, form validation, pagination, custom CLI commands, error handling, and more.
Features
Factory Pattern for clean app structure and easier testing

🗄️ SQLAlchemy for ORM and database management

📧 Flask-Mail for sending emails

🔌 Flask-Login for user authentication and session management

🧠 Flask-WTF for secure and validated forms

📦 Blueprints for modular code organization

📤 Image Upload with secure file handling

📄 Pagination for handling large lists efficiently

✅ Custom CLI Commands (e.g., for creating superusers)

🧪 Validation logic for form and input fields

📛 Error Handlers for custom error pages (404, 500, etc.)

🔐 Dotenv for environment variable management

📝 Logging to file for error tracking and debugging

Project Structure
/healthcare/
│
├── __init__.py           # create_app() is defined here
├── app.py                # Application entry point
├── app.log               # Application log
├── config.py             # Configuration settings
├── .env                  # Enviornment file
├── extensions.py         # Initialize Flask extensions
├── home/                 # Home blueprint
├── auth/                 # Authentication blueprint
│   ├── cli.py            # Custom CLI command (e.g., create_superuser)
│   ├── hooks.py          # Request hooks (e.g., JWT or session handling)
|   ├── templates         # Jinja2 HTML templates
|   ├── models.py         # SQLAlchemy models
|   ├── forms.py          # WTF forms
|   ├── routes.py         # Function based views 
├── doctors/              # Doctors blueprint
├── services/             # Services blueprint
├── appointments/         # Appointments blueprint
├── templates/            # Jinja2 HTML templates
├── static/               # Static files (CSS, JS, images)
└── error_pages/          # Custom error pages

Setup Instructions
1. 📦 Create Virtual Environment and Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
2. 🔐 Set Environment Variables
Create a .env file in the project root and add:
SECRET_KEY=your_secret_key
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_email_password
UPLOAD_FOLDER=static/uploads

Basic Run:
flask run

Run in Debug Mode:
flask --debug run

CLI Commands
flask create-superuser

