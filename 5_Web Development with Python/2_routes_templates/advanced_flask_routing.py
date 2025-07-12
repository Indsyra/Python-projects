from flask import Flask

app = Flask(__name__)

# Static route
@app.route('/home')
def home():
    return "Welcome to My Blog!"

# Dynamic Route
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Displaying Post #{post_id}"

if __name__ == '__main__':
    app.run(debug=True)