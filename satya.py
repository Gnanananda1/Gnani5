from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'Gnani@1793'  # Replace with your secret key

# Flask-Login initialization
login_manager = LoginManager()
login_manager.init_app(app)

# User class for authentication
class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password

# Simulated user database (replace with your actual database)
users = {'Gnani': {'password': 'Gnani@1744'}}  # Modify with your username and password

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id, users[user_id]['password'])
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        if user.id in users and users[user.id]['password'] == user.password:
            login_user(user)
            return redirect(url_for('receipt'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/receipt', methods=['GET', 'POST'])
@login_required
def receipt():
    if request.method == 'POST':
        # Get user inputs from the form
        name = request.form['name']
        dob = request.form['dob']
        # Process the form data as needed
        return render_template('receipt.html', name=name, dob=dob)
    return render_template('receipt_form.html')

if __name__ == '__main__':
    app.run(debug=True)
