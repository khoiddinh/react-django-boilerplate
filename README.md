Note: only use npm for package handling in this repo (DO NOT USE YARN).

BACKEND SETUP:

First, cd into backend and create and activate a venv:
python3 -m venv venv
source venv/bin/activate
Then, install the requirements using pip:
pip install -r requirements.txt

Create a .vscode directory in the outermost directory (where backend, frontend dirs are)
Make a settings.json file with these contents:
{
  "python.defaultInterpreterPath": "backend/venv/bin/python3",
  "python.analysis.extraPaths": ["backend"]
}

Then, open vscode search (CMD+Shift+P/Ctrl+Shift+P) and type python interpreter. Press enter, and select Use Python from python.defaultInterpreterPath setting. If it's not there, search "Developer: reload window" and refresh a couple of times. Once you've delected the python interpreter, refresh again until the import errors go away.

Create .env file in /backend dir using .env.example as a template

FRONTEND SETUP:

Then, cd into frontend. Run npm ci (NOT npm install). If you are modifying package-lock.json you are doing it wrong.

To run both the frontend and backend in a local development environment:
cd into /frontend directory (all commands run in frontend dir)
run: npm run start:full
To just run the backend, run: npm run dev
A full list of commands can be found in package.json in "scripts"



Other TIPS:

Making routes:
Build routes in core/views.py
Then add them to config/urls.py



