import sqlalchemy
from sqlalchemy import create_engine, text
db_connection_string="mysql+pymysql://sql5676383:2xDB9Xw9lm@sql5.freesqldatabase.com/sql5676383?charset=utf8mb4"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())
  print(result_dicts)