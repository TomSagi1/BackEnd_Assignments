from flask import redirect, render_template, request, Blueprint
from db import db_Assignment10

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')

message = ""


@assignment10.route("/assignment10", methods=['GET', 'POST'])
def assignment10():
    global message
    message = ""
    return render_template('assignment10.html')


# insert user
@assignment10.route('/insert_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    db_Assignment10(query=query, query_type='commit')
    global message
    message = name + " was inserted"
    return redirect('/list')


# update user
@assignment10.route('/update_user', methods=['POST'])
def update_user():
    name = request.form['name']
    new_email = request.form['new_email']
    query = "update users set email = '%s' where name = '%s'" % (new_email, name)
    db_Assignment10(query=query, query_type='commit')
    global message
    message = name + "'s email is updated"
    return redirect('/list')


# delete user
@assignment10.route('/delete_user', methods=['POST'])
def delete_user():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s'" % name
    db_Assignment10(query, query_type='commit')
    global message
    message = name + " was deleted"
    return redirect('/list')


# show users
@assignment10.route('/list')
def users_list():
    query = "select * from users"
    query_result = db_Assignment10(query=query, query_type='fetch')
    return render_template('assignment10.html', list=query_result, message=message)
