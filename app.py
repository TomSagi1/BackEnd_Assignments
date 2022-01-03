from flask import Flask, redirect, url_for, render_template
from flask import request, session, Blueprint


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
    name = 'Tom Sagi'
    hobbies = ["sports", "reading", "cooking", "surfing"]
    return render_template("assignment8.html", name=name, hobbies=hobbies)


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_page():
    users = {'user1': {'user_name': 'tomsag', 'email': 'tomsag@post.bgu.ac.il'},
             'user2': {'user_name': 'superman', 'email': 'superman121@gmail.com'},
             'user3': {'user_name': 'lebronJ', 'email': 'LebronJames@gmail.com'},
             'user4': {'user_name': 'RogerF', 'email': 'rogerf@gmail.com'},
             'user5': {'user_name': 'TheRock', 'email': 'rocking1993@gmail.com'}
             }
    # Get method for searching
    if request.method == "GET":
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name == '':
                return render_template('assignment9.html', list=users)
            for key, value in users.items():
                if value.get('user_name') == user_name:
                    return render_template('assignment9.html', user_name=value.get('user_name'),
                                           user_email=value.get('email'))
    # Post method for registration
    if request.method == "POST":
        session['user_name'] = request.form['user_name']
    return render_template('assignment9.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session['user_name'] = ''
    return render_template('assignment9.html')


#  assignment10
from pages.assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


@app.route('/about')
def about_page():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

