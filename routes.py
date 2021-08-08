from flask import Blueprint, render_template, url_for, request
import trend
import indices
from send_mail import send_mail
import threading





main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index_min.html', trend=trend)

@main.route('/about')
def about():
    return render_template('about_min.html')

@main.route('/strategies')
def strategies():
    return render_template('strategies_min.html', indices=indices)

@main.route('/contact')
def contact():
    return render_template('contact_min.html')

@main.route('/success',methods=['GET', 'POST'] )
def success():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        t1 = threading.Thread(target=send_mail, args=[email])
        t1.start()
        return render_template('success_min.html', name=name, email=email)

    
@main.app_errorhandler(404)
def not_found(e):
    return render_template('404_min.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500_min.html'), 500



