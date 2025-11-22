from flask import Flask, redirect, url_for, render_template, request
from select_price import select_price


app = Flask(__name__)


@app.route("/", methods=['Get'])
def home():
    #return render_template('index.html') 
    data, column_names = select_price()
    return render_template('index.html')

@app.route('/select_price')
def select_price1():
       data, column_names = select_price()
       return render_template('get_prices.html', data=data, column_names=column_names)

if __name__ == "__main__":
    app.run(debug=True)