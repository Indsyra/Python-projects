from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Handling User Registration
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


# Create Database Tables
with app.app_context():
    db.create_all()


# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            flash('All field are required', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('Username or Email already exists!', 'error')

    return render_template('register.html')


# Login Route (Placeholder)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('All field are required', 'error')
            return redirect(url_for('login'))

        user = db.session.get(User, {"username": username})
        if not user or (user and not check_password_hash(user.password, password)):
            flash('Incorrect username or password', 'error')
            return redirect(url_for('login'))
        flash('Successful Login', 'success')
        return render_template('home.html', username=username)
    return "Login Page (To be implemented)"


# Home Page
@app.route('/home')
def home(username):
    


if __name__ == '__main__':
    app.run(debug=True)