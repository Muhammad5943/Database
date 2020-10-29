from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData, Table

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
print(engine.table_names())

metadata = MetaData()
census = Table('census',metadata,autoload=True,autoload_with=engine)
print(repr(census))