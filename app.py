from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route("/", methods=['Get'])
def home():
    #return '<a href="/run_script">Add new employee</a>'
    return render_template('index.html') 


if __name__ == "__main__":
    app.run(debug=True)