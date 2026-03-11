from flask import Flask

# WSGI application
app = Flask(__name__)   # instance of Flask class, which will be our WSGI (Web Server Gateway Interface) application.

# creating a basic rount
# home page

@app.route("/")
def welcome():
    return 'welcome to this flask course. This should be fun. Alright myan!'

@app.route("/index")
def index():
    return 'welcome to the index page'




if __name__ == "__main__":
    app.run(debug=True)