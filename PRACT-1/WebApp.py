from flask import Flask

# Creating a Flask web application instance
app = Flask(__name__)

# Defining a route; Routes define which URL triggers which function.

@app.route("/")
def hello():
    return "Hello, World!"

# Running the application
if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080, debug=True)

    #app.run() only executes when running the script directly and prevents unintended behavior when importing
    #host="0.0.0.0": Makes the app accessible over the Local  network.
    #port=8080: Runs the app on port 8080 instead of the default 5000.
    #debug=true : Enables auto-reload and error messages (for development).


