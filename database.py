from sqlalchemy import create_engine,text
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
