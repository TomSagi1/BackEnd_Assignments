from flask import Flask , redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'This is where we begin'

@app.route('/about')
def about_page():
    return redirect('/')

@app.route('/catalog')
def catalog_page():
    return 'This will be a catalog page :)'

@app.route('/transfer')
def urldirect_page():
    return redirect(url_for('catalog_page'))

if __name__ == '__main__':
    app.run(debug=True)
