from flask import*
public=Blueprint('public',__name__)
@public.route('/')
def home():
    return render_template('home.html')
@public.route('/login')
def login():
    if 'login' in request.form:
        username=request.form['username']
        passw=request.form['password']
    return render_template('login.html')