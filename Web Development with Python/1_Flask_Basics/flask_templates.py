from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)


# Define a route (URL)
@app.route('/')
def hello():
    return render_template('index.html', name="Flask Developer")


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
    # Start the flask development server with debugging enabled