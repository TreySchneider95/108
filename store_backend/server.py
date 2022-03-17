from flask import Flask

app = Flask('server')

@app.route("/")
def home():
    return "hello from flask"

@app.route("/me")
def about_me():
    return "Trey Schneider"
    
app.run(debug=True)