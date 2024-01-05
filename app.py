from flask import Flask, render_template, jsonify

app=Flask(__name__)
JOBS=[
  {
    'job_id':1,
    'title':'Data Analyst',
    'location':'New York, NY',
    'salary': '$100,000'
  },
  {
    'job_id':2,
    'title':'Software Engineer',
    'location':'San Francisco, CA',
    'salary': '$150,000'
  },
  {
    'job_id':3,
    'title':'Data Scientist',
    'location':'San Jose, CA',
    'salary': '$170,000'
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def jobs_list():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)