from sqlalchemy import create_engine, text, insert, Table, MetaData
from sqlalchemy.orm import sessionmaker

db_connection_string="mysql+pymysql://sql5676383:2xDB9Xw9lm@sql5.freesqldatabase.com/sql5676383?charset=utf8mb4"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    list = []
    for row in result.all():
      list.append(row._asdict())
    return list

  
def load_job_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text(f"select * from jobs where id = {id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
    

def add_application_to_db(job_id, data):
  
  with engine.connect() as conn:
      query = text("""
          INSERT INTO application
          (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
          VALUES
          (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url) """)
  
      params = {
          'job_id': job_id,
          'full_name': data['full_name'],
          'email': data['email'],
          'linkedin_url': data['linkedin_url'],
          'education': data['education'],
          'work_experience': data['work_experience'],
          'resume_url': data['resume_url']
      }
  
      print(f"Executing Query: {query}, Params: {params}")
      result = conn.execute(query, params)
  
      print(f"Rows Affected: {result.rowcount}")





     

      

     


