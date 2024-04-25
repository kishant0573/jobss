from flask import Flask , render_template,request,jsonify
from database import load_jobs_from_db,load_data_for_id,save_to_db
app = Flask(__name__)

@app.route("/")
def first():
    job = load_jobs_from_db() 
    return render_template('home.html',jobs=job)

@app.route("/job/<id>")
def job_id(id):
    data = load_data_for_id(id)
    return render_template('jobinfo.html', data=data)

# @app.route("/job/<id>/apply")     #without post method for job apply
# def job_apply(id):
#     form_data = request.args
#     return form_data

@app.route("/job/<id>/apply" ,methods=['post'])     #with post method for job apply
def job_apply(id):
    job = load_data_for_id(id)
    form_data = request.form
   # Convert ImmutableMultiDict to regular dictionary
    data_dict = dict(form_data)
    save_to_db(id,data=data_dict)
    return render_template('application_submit.html',data=data_dict,job=job)
if __name__ == '__main__':
    app.run(debug=True,port=8000)                  #we can change port also port = 8000 and host also host = :"0.0.0.0"