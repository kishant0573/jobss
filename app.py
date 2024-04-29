from flask import Flask , render_template,request,jsonify,redirect,flash,session,render_template_string
from database import load_jobs_from_db,load_data_for_id,save_to_db,logins,register,count_application,show_in_table,categories,admin_login,add_jobs
from functools import wraps

app = Flask(__name__)
app.secret_key = 'key'

@app.route("/")
@app.route("/home")
def first():
    job = load_jobs_from_db() 
    return render_template('home.html',jobs=job)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_login' not in session:
            return render_template('admin_login.html')
        return f(*args, **kwargs)
    return decorated_function


@app.route("/job/<id>")
@login_required
def job_id(id):
    data = load_data_for_id(id)
    return render_template('jobinfo.html', data=data)

# @app.route("/job/<id>/apply")     #without post method for job apply
# def job_apply(id):
#     form_data = request.args
#     return form_data

@app.route("/job/<id>/apply" ,methods=['post'])     #with post method for job apply
@login_required
def job_apply(id):
    job = load_data_for_id(id)
    form_data = request.form
 
    data_dict = dict(form_data)
    save_to_db(id,data=data_dict)
    return render_template('application_submit.html',data=data_dict,job=job)
   

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect('/login')

@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_login', None)
    return redirect('/home')

@app.route("/authenticate" ,methods=['post','get'])
def authenticate_user():
    data = request.form
    new_data = logins(user_id=data['user_id'],password=data['password'])
    if new_data:
        session['logged_in'] = True
        session['username'] = data['user_id']
        return redirect('/home')
    else:
        flash("Please enter correct username and password")
        return redirect('/login')
   

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/admin/login',methods=['POST','get'])
def admin_login_route():
    data = request.form
    
    result = admin_login(user_id=data['user_id'],password=data['password'])
    # return result
    if result:
        session['admin_login'] = True
        return redirect('/admin')
    flash("enter valid userid and password")
    return redirect('/admin')


@app.route('/admin',methods=['GET','post'])
@admin_login_required
def admin():
    data = count_application()
    result = show_in_table()
    result_categories = categories()
    # return result_categories
    return render_template('admin.html',data=data['count(*)'],result=result,result_categories=result_categories)


@app.route("/register_user",methods=['post','get'])
def register_user():
    if request.method == 'POST':
        data = request.form
        x  =  register(user_id=data['user_id'],user_name=data['user_name'],password=data['password'])
        if x  == False:
            flash("email is already registered")
            return redirect('/signup')
        else:
            flash('You are registered! Please log in.')
            return redirect('/signup')
    else:
        return render_template('login.html')


@app.route('/add_job',methods=['POST','get'])
@admin_login_required
def add_job():
    return render_template('add_job.html')

@app.route('/add_job_db',methods=['POST','get'])
@admin_login_required
def add_job_db():
    data = request.form
    add_jobs(title= data['title'],location= data['location'],salary= data['salary'],currency= data['currency'],requirements= data['requirements'],responsibility = data['responsibility'])
    return redirect('/admin')
if __name__ == '__main__':
    app.run(debug=True,port=8000)                  #we can change port also port = 8000 and host also host = :"0.0.0.0"