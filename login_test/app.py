from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login_test/templates/login.html', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Verifica credenciais (para fins de teste, use um usuário e senha fixos)
    if username == "admin" and password == "password":
        return "Login bem-sucedido!"
    else:
        return "Usuário ou senha inválidos!", 401

if __name__ == '__main__':
    app.config['SERVER_NAME'] = 'localhost:5000'  # Ensure this matches the host and port
    app.run(debug=True, host='0.0.0.0', port=5000)  # Modificado para permitir conexões de qualquer IP
