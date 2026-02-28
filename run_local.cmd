@echo off
REM launcher script for local development on Windows
REM run this from the project root (it should be placed there)

REM activate the virtual environment
call "%~dp0env\Scripts\activate.bat"

REM ensure we're in the project directory
cd /d "%~dp0"

REM apply any pending migrations (optional but convenient)
python manage.py migrate

REM open the default browser on the development URL
start http://127.0.0.1:8000

REM run Django's development server on localhost
python manage.py runserver
