from flask import Flask, request 
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

        </style>
    </head>
    <body>
      <form method="post">
        <label>
         Signup:<br> 
            Username:  
            <input type="text" name="username" minlength="3" maxlength="20" required/><br>
            Password:
            <input type="password" name="password" minlength="3" maxlength="20" required/><br>
            Verify Password:
            <input type="password" name="verify" minlength="3" maxlength="20" required/><br>
            Email (optional)  
            <input type="text" name="email (optional)" minlength="3" maxlength="20"/><br>
        
            
        </label>
        <input type="submit"/>
    </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def psw_verify():
    password = request.form['password']
    orig_password = request.form['password']
    verify_password = request.form['verify']
    username = request.form['username']
    for password in password:
        if orig_password == verify_password:
            return ("Welcome, " + username + "!")
        else:
            return "Passwords must match!" 
  
app.run()