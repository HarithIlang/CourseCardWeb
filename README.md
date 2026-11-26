# CourseCardWeb

CSC 226 final project at CSI: a website where students save their class schedule, rooms, professors, and office hours in one place.

Built with Python + Django, plain HTML + CSS pages, and a SQLite database. These steps are for **Windows 10 and 11** and use **VS Code**.

## Pick your path

- **Path A: I just want to run the site.** You download a ZIP. No GitHub account needed.
- **Path B: I'm working on the code.** You use GitHub Desktop. You need a free GitHub account.

Both paths use the same steps. Only Step 3 (getting the code) is different.

---

## Step 1: Install Python (one time)

First check if you already have it. Press the Windows key, type `cmd`, press Enter. In the black window, type:

```
python --version
```

- If it says **Python 3.12, 3.13, 3.14 or 3.15**, you are done. Go to Step 2.
- If it says "Python was not found", opens the Microsoft Store, or shows a number lower than 3.12, install Python:
    1. Go to https://www.python.org/downloads/release/python-31410/ (Python 3.14.10, the version this project was built with).
    2. Scroll to the Files table, click **Windows installer (64-bit)**, and run it.
    3. On the first screen, tick the box at the bottom that says **Add python.exe to PATH**. Then click **Install Now**. (This box is how VS Code finds Python later.)
    4. Close the black window, open a new one, and run `python --version` again. You should see `Python 3.14.10`.

---

## Step 2: Install VS Code (one time)

If you already have VS Code, skip to Step 3. If not, go to https://code.visualstudio.com, click the Windows download, run it, and keep the default choices.

---

## Step 3: Get the code (pick ONE)

### Path A: ZIP

1. Go to https://github.com/HarithIlang/CourseCardWeb
2. Click the green **Code** button, then **Download ZIP**.
3. Open your Downloads folder. Right-click the ZIP file and choose **Extract All...**, then **Extract**. (The files do not work from inside the ZIP. You must extract them.)
4. Do NOT put the folder inside OneDrive. OneDrive tries to sync the thousands of files that Step 5 creates and can break things. A plain folder like `C:\CourseCardWeb` is safe: type that in the Extract box.
5. Open the extracted folders until you see a file named **manage.py**. That folder is your **project folder**. (Windows often makes a folder inside a folder with the same name, so you may need to open two.)

### Path B: GitHub Desktop

1. Install GitHub Desktop from https://desktop.github.com and sign in with your GitHub account. (It already includes Git. You do not need to install Git yourself.)
2. In GitHub Desktop, click **File**, then **Clone repository...**, then the **URL** tab.
3. In the box, paste `https://github.com/HarithIlang/CourseCardWeb`
4. Under **Local path**, check the folder. If the path contains the word **OneDrive**, click **Choose...** and pick a plain folder like `C:\GitHub` instead. (Same reason as the ZIP steps above: OneDrive can break the setup.)
5. Click **Clone**. The folder you just made (it has **manage.py** inside) is your **project folder**.

---

## Step 4: Open the project in VS Code and open its terminal

1. Open VS Code, click **File**, then **Open Folder...**, and pick your project folder (the one that shows manage.py). If you used GitHub Desktop, its **Open in Visual Studio Code** button does the same thing.
2. If VS Code asks whether you trust the authors of the files in this folder, click the **Yes** button. VS Code will not open a terminal until you do.
3. Open the terminal: click **Terminal** in the top menu, then **New Terminal**. (If you don't see Terminal in the menu, click the three dots **...** at the end of the menu first. The keyboard shortcut is to hold Ctrl and press the backtick key, which is the key above Tab.)
4. A terminal opens at the bottom. It should already be inside your project folder: the line starts with `PS` and ends with the folder name, like `PS C:\CourseCardWeb\CourseCardWeb-main\CourseCardWeb-main>`. Type `dir` and press Enter. You should see **manage.py** in the list. If you don't, see "If something goes wrong".

---

## Step 5: First-time setup (about 2 minutes, needs internet)

In the VS Code terminal, type one line, press Enter, and wait for the next prompt before typing the next line.

**5a. Make a private box of Python tools just for this project:**

```
python -m venv venv
```

It prints nothing and takes a few seconds. (VS Code may pop up a small box about the new environment. Clicking Yes is fine.) If `python` doesn't work but `py --version` does, type `py -m venv venv` here instead. Everything else stays the same.

**5b. Turn the box on:**

```
venv\Scripts\activate
```

Your line should now start with **(venv)**. You have to do this each time you open a new terminal.

If you get red text saying **"running scripts is disabled on this system"**: Windows blocks PowerShell scripts by default. Run this once, answer `Y` if it asks, then run `venv\Scripts\activate` again:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**5c. Install the exact tools the project uses:**

```
python -m pip install -r requirements.txt
```

The last line should say `Successfully installed Django-6.1.3 ...`

**5d. Build the database:**

```
python manage.py migrate
```

You should see a list of lines that all end in `OK`.

---

## Step 6: Start the site

```
python manage.py runserver
```

Leave the terminal open. Hold **Ctrl** and click the `http://127.0.0.1:8000/` link in the terminal, or type that address into a browser.

You should see Django's **"The install worked successfully!"** page (this page will change as we build the site).

To stop the site: click inside the terminal and press **Ctrl+C**. (If it doesn't stop, click the trash can icon at the top of the terminal, then open a new terminal.)

---

## Next time (after the first time)

Open VS Code. It usually reopens your project. If not, click **File**, then **Open Recent**, and pick it. Open a terminal (Step 4, number 3), then:

```
venv\Scripts\activate
python manage.py runserver
```

**If you use GitHub Desktop:** before that, open GitHub Desktop and click **Fetch origin**. If it turns into **Pull origin**, click it. After every pull, also run these two lines before `runserver`. They are safe to run even if nothing changed:

```
python -m pip install -r requirements.txt
python manage.py migrate
```

**If you downloaded the ZIP:** to get newer code, download a new ZIP and repeat Step 3 into a new folder. Your database will start empty again.

---

## Working together (GitHub Desktop)

1. At the start of each work session: **Fetch origin** in GitHub Desktop, then **Pull origin** if it appears.
2. Make your changes in VS Code and save the files.
3. In GitHub Desktop, your changed files show on the left. Write a short summary of what you did (bottom left), then click **Commit to main**.
4. Click **Push origin** at the top. Now your partner can pull your work.
5. Push small, working changes often.
6. Only one person should change `models.py` at a time. If two people change it together, Django can make two clashing database files.
7. `venv` and `db.sqlite3` stay on your own PC and are never pushed. Everyone has their own database.
8. To add a new package: run `python -m pip install <name>`, then `python -m pip freeze | Out-File requirements.txt -Encoding ascii`, then commit `requirements.txt`. (The `Out-File ... -Encoding ascii` part matters: plain `>` in PowerShell saves the file in a format that looks garbled on GitHub.)

---

## If something goes wrong

**"Python was not found", or the Microsoft Store opens, or `'python' is not recognized`**
Python is missing, or the PATH box wasn't ticked. Try `py --version`. If that works, use `py` instead of `python` for the `venv` line only. If not, uninstall Python (Settings, Apps, Installed apps), then redo Step 1 and tick the box. If the Store still opens, press the Windows key, search **Manage app execution aliases**, and switch off the two entries named **App Installer** for python.exe and python3.exe.

**Red text saying "running scripts is disabled on this system"**
Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once (see Step 5b), then try again.

**VS Code won't open a terminal, or says the folder is not trusted**
Click **Trust** (or **Yes**) when VS Code asks about the folder. VS Code blocks the terminal until you do.

**`ImportError: Couldn't import Django` (or your line doesn't start with `(venv)`)**
The box isn't turned on. Run `venv\Scripts\activate`, then try again. If it still fails, run `python -m pip install -r requirements.txt` again.

**`can't open file ... manage.py ... No such file or directory`, or `dir` doesn't show manage.py**
Wrong folder. In VS Code, click **File**, then **Close Folder**, then open the folder that shows **manage.py** (Step 4). Then open a new terminal.

**`No matching distribution found for Django==6.1.3`**
Your Python is older than 3.12 (see Step 1), or you have no internet.

**`Error: That port is already in use.`**
The site is already running in another terminal (stop it there), or another program uses port 8000. Run `python manage.py runserver 8080` and open http://127.0.0.1:8080/ instead.

**The browser says it can't connect**
The site isn't running. Look at the terminal: it must still be open, with no error. If you closed it, redo Step 6 (turn the box on first).

**`You have 18 unapplied migration(s)` in the terminal**
You skipped the database step. Run `python manage.py migrate`.

**Things act strangely after moving or copying the folder**
Delete the `venv` folder and redo Step 5. It is safe: everything in `venv` gets rebuilt. Never copy `venv` from another computer.

**GitHub Desktop says your push was rejected**
Click **Fetch origin**, then **Pull origin**, then **Push origin** again. If it shows a merge conflict, stop and message your partner before clicking anything else.

---

## Notes

- Built and tested with Python 3.14. Django 6.1.3 supports Python 3.12 to 3.15.
- No VS Code? Command Prompt works too. Open the project folder in File Explorer, click the address bar, type `cmd`, press Enter, and use the same commands from Step 5. In Command Prompt, Step 5b needs no policy change.
