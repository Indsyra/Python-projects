from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)


# Define a route (URL)
@app.route('/')
def home():
    return render_template('index1.html')


@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)


@app.errorhandler(404)
@app.route('/about')
def about():
    return render_template('about.html')


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
    # Start the flask development server with debugging enabled