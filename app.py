# Here this is the main file for our project in which we will write all our important code here

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Project Name  :- "AttendifyX : Intelligent AI Attendance System"
# It uses face and voice recognition for marking whether user is present or not.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Flask :- 
# It is a python framework used for building web applications.
# The primary work of flask is to write the server side code.

# Flask is a lightweight Python web framework used to build web applications and APIs. It’s simple, flexible, and often chosen for small to medium projects where developers want control over the architecture without heavy dependencies.

# Key Features of Flask :-
# - Microframework: Minimal design with only core features; developers add extensions as needed.
# - Routing: Easy URL mapping using decorators (@app.route).
# - Request Handling: Manages HTTP requests and responses via the Werkzeug toolkit.
# - Template Rendering: Uses Jinja2 for dynamic HTML generation.
# - Flexibility: No built-in ORM; you can use SQLAlchemy, raw SQL, or any database library.
# - Extensible: Large ecosystem of community extensions (authentication, database integration, etc.).

# SO we firstly need to install it using :- pip install flask

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Now flask requires an entry point which is this app.py file actually
# Now in this python file, we will write all our API endpoints i.e routes
# We can name this file as app.py or main.py but we don't give it name as flask.py because flask is a module in itself & not a file.


from flask import Flask, render_template
# Here we are importing this Flask class and we will use it to create this app

# Here this is web app i.e application which will take request & give some response
app = Flask(__name__)
# Flask(__name__) creates a new Flask web application object.
# The __name__ variable tells Flask where to look for resources (like templates or static files). It helps Flask know the “root path” of your app.
# This app object is the central piece: it handles incoming requests and sends back responses.


# here this is the root URL i.r route => endpoints
@app.route("/")
def home():
    # So whenever request is coming to this home url, it will render this index.html page & return the response 
    return render_template('index.html')




# standard way to run a Flask app safely.
if __name__ == "__main__":
    app.run(debug=True, port=5002)
    # This line starts the Flask development server.
    # By default, Flask runs on http://127.0.0.1:5000/ (localhost, port 5000). 
    # Once you run this, Flask begins listening for incoming HTTP requests.
    # But here it will run on 5002 port

# debug=True Flag :-
# - Debug mode is a special setting for development:
# - Auto-reload: If you change your code and save, Flask automatically restarts the server. You don’t need to stop and restart manually.
# - Detailed error pages: If something goes wrong, Flask shows a helpful debugger in the browser with stack traces and variable inspection.
# - This makes development faster and easier, but it should not be used in production because:
# - It exposes sensitive information in error pages.
# - It can allow arbitrary code execution if misused.


# In Python, every file has a special private variable called __name__.
# If you run a file directly (like python app.py), then __name__ is set to "__main__".
# If the file is imported into another script (e.g., for testing or as part of a bigger project), then __name__ is set to the module’s name (like "app").
# This check ensures that the server only starts when you run the file directly, not when it’s imported elsewhere.

# Why This Matters :-
# - Without this guard, if another script imports your Flask app, it would immediately start the server, which is usually not what you want.
# - With the guard, you can safely import app into other files (for testing, WSGI deployment, etc.) without triggering app.run().

# Now we can run this file using :- python app.py

# SO now we can run the flask app using :-
# python app.py
# ----------OR--------
# flask --app app run --debug

