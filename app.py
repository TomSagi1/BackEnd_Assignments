from flask import Flask, redirect, url_for, render_template
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'


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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    search = ''
    user_name = ''
    users = {'user1':{'user_name': 'tomsag', 'email': 'tomsag@post.bgu.ac.il'},
             'user2':{'user_name': 'superman', 'email': 'superman121@gmail.com'},
             'user3':{'user_name': 'lebronJ', 'email': 'LebronJames@gmail.com'},
             'user4':{'user_name': 'RogerF', 'email': 'rogerf@gmail.com'},
             'user5':{'user_name': 'TheRock', 'email': 'rocking1993@gmail.com'}
             }
    method = request.method
    if method == 'GET':
        if 'searchIn' in request.args:
            search = request.args['searchIn']
            return render_template('assignment9.html', search=search, users=users)
    if method == 'POST':
        user_name = request.form['user_name']
        session['logged_in'] = True
        session['user_name'] = user_name
    return render_template('assignment9.html', request_method=request.method, user_name=user_name)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    session['user_name'] = ''
    return redirect(url_for('assignment9'))


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
