from flask import request

def auth(app, user):
    @app.route('/login', methods=['POST'])
    def login():
        values = request.values
        username = values.get('username')
        password = values.get('password')
        return user.login(app, username, password)