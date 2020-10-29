from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, String, select
from sqlalchemy import or_

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload = True, autoload_with = engine)
stmt = select([census])

# filtering data with 'Calfornia' key
""" stmt = stmt.where(census.columns.state == 'California')
results = connection.execute(stmt).fetchall()
for result in results:
    print(result.state, result.age) """

# filtering data with startwith('New')
""" stmt = stmt.where(census.columns.state.startswith('New'))
results = connection.execute(stmt).fetchall()
for result in connection.execute(stmt):
    print(result.state, result.pop2008) """

# filtering with or_ function
stmt = stmt.where(
    or_(    
        census.columns.state == 'California',
        census.columns.state == 'New York'
    )
)

results = connection.execute(stmt).fetchall()
for result in results:
    print(result.state, result.sex)