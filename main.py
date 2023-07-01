from flask import Flask, render_template, url_for
app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

app.run(host='0.0.0.0', port=8080)
