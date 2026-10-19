Flask Hello Site

This is a Flask site which greets one on entering their name.

In this, HTML, CSS, JS, Flask (python) is used. This is a demonstration that how to integrate HTML, CSS, JS with the backend Flask.

The Project structure is:

Site_Hello!
│
├── app.py                # Main Flask backend file
├── templates/            # Folder strictly for HTML files
│   └── index.html
└── static/               # Folder for CSS, JavaScript, and images
    ├── style.css
    └── script.js

(with Flask we use this project structure because Flask this only and it has also become thr convention now..with FastApi, etc.)

Following are the commands one can use for integration:-
1. open terminal in VSCode -> 'ctrl' + '~'
2. Create a Virtual environment and activate it.
   a) python -m venv venv    {creation of virtual environment}
   b) venv\Scripts\activate  {for activation}
3. install relevant/required libraries
   a) pip install flask
4. Create your main.py file to initialize the Flask application and create a route that renders your main HTML page
5. write html, css, js -> Inside the templates/ folder, create index.html.
   To link your CSS and JavaScript files from the static folder, you must use Flask’s url_for() function instead of standard relative paths
6. open terminal in your editor 
7. write Flask run in terminal -> you will get an http address
8. Copy that address and paste it in your browser and open it.
9. And your page is in front of you!
