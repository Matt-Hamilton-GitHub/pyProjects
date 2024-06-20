from flask  import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h1>Welcome to Main Page</h1>'

@app.route('/users/<user_name>')
def user_page(user_name):
    return f'<h3>Welcome, {user_name.upper()} !</h3>'

if __name__ == '__main__':
    app.run(debug='true')