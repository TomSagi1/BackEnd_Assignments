from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("cv.html")


@app.route('/contact')
def catalog_page():
    return render_template("cv1.html")


@app.route('/assignment8')
def assignment8():
    name = "Tom Sagi"
    hobbies = ["sports", "reading", "cooking", "surfing"]
    return render_template("assignment8.html", name=name, hobbies=hobbies)


@app.route('/about')
def about_page():
    return redirect('/')


@app.route('/catalog')
def catalog_page():
    return 'This will be a catalog page '


@app.route('/transfer')
def urldirect_page():
    return redirect(url_for('catalog_page'))


if __name__ == '__main__':
    app.run(debug=True)

    
