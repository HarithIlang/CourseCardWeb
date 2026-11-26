# CourseCardWeb
CSC 226 final project at CSI: a website where students save their class schedule, rooms, professors, and office hours in one place.

Built with Python + Django, plain HTML + CSS pages, and a SQLite database.

## Setup on Windows (first time)

You need **Python 3.14** (Django 6.1 works with Python 3.12 to 3.14, not 3.15) and **Git**.

Run these in the VS Code terminal (PowerShell), one at a time:

1. Clone the repo and open the folder in VS Code:
   ```
   git clone https://github.com/HarithIlang/CourseCardWeb.git
   cd CourseCardWeb
   ```
2. Make the virtual environment (a private set of Python packages just for this project):
   ```
   python -m venv venv
   ```
3. Turn it on. The line should then start with `(venv)`:
   ```
   venv\Scripts\activate
   ```
   If you get red text saying "running scripts is disabled on this system", run this once, then try step 3 again:
   ```
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
4. Install the exact package versions the project uses:
   ```
   pip install -r requirements.txt
   ```
5. Build the database tables (your database starts empty; it is not shared through GitHub):
   ```
   python manage.py migrate
   ```
6. Optional: make an admin login for the /admin page:
   ```
   python manage.py createsuperuser
   ```
7. Start the site, then open http://127.0.0.1:8000/ in a browser. Stop it with Ctrl+C:
   ```
   python manage.py runserver
   ```

## Every time after that

Open the folder in VS Code, run `venv\Scripts\activate`, then `git pull` to get the latest changes. If someone changed the models, run `python manage.py migrate` again before `runserver`.

## Notes

- `venv/` and `db.sqlite3` are never pushed (the .gitignore skips them).
- If you install a new package, update the list with:
  `pip freeze | Out-File requirements.txt -Encoding ascii`
  (plain `pip freeze > requirements.txt` in PowerShell saves the file in a format that can look garbled on GitHub).
