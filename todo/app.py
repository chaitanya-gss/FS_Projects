from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key
login_manager = LoginManager()
login_manager.init_app(app)

# Mock User class for demonstration (replace with your actual User model)
class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

# Mock user database (replace with your actual user management logic)
users = {'user1': {'password': 'password1'}}

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None

@app.route('/')
@login_required
def index():
    # Example lists data to pass to the template
    lists = [
        {'title': 'List 1', 'tasks': ['Task 1', 'Task 2']},
        {'title': 'List 2', 'tasks': ['Task 3', 'Task 4']}
    ]
    return render_template('index.html', lists=lists)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and request.form['password'] == users[username]['password']:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return 'Login Failed. Invalid username or password.'
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
