# Library App

A simple library app whit which users can browse books and see the due dates of their borrowed books. Librairians can additionally modify, add or delete books from the library's catalog.

The application was build using the Django Web framework and by following the [Django Tutorial from MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django).

## Run Locally

### Prerequisites
- Python 3
- `pip`
- `git`

### Setup
1. Clone the repository and go to the project folder:
   ```bash
   git clone https://github.com/btaskinen/django-library.git
   cd django-library
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows (PowerShell), activate with:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install "Django>=6.0,<6.1"
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the app in your browser:
   - App: http://127.0.0.1:8000/catalog/
   - Admin: http://127.0.0.1:8000/admin/

### Run Tests
```bash
python manage.py test
```
