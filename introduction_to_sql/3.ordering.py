from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, select
from sqlalchemy import desc

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload = True, autoload_with = engine)
# show view the 10 data in census table 
""" stmt = select([census.columns.state])
results = connection.execute(stmt).fetchall()

print(results[:10]) """

# order census table data
""" stmt = select([census.columns.state])
stmt = stmt.order_by(census.columns.state)
results =connection.execute(stmt).fetchall()
print(results[:10]) """

# order census table data in desc
""" stmt = select([census.columns.state])
stmt = stmt.order_by(desc(census.columns.state))
result = connection.execute(stmt).fetchall()

print(result[:10]) """

# ordering data with 2 params state and sex in census table
stmt = select([census.columns.state, census.columns.sex])
stmt = stmt.order_by(census.columns.state, census.columns.sex)
result = connection.execute(stmt).first()
print(result)

# untuk melihat query
print(stmt)