from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, select
from sqlalchemy import func

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload = True, autoload_with = engine)

# How to summing value of data
""" stmt = select([func.sum(census.columns.pop2008)])
results = connection.execute(stmt).scalar()

print(results) """

# Grouping from data
# TODO: stmt = select([column selected1, column selected2,...])
""" stmt = select([census.columns.sex, func.sum(census.columns.pop2008)])
stmt = stmt.group_by(census.columns.sex)
results = connection.execute(stmt).fetchall()

print(results) """

stmt = select([census.columns.sex, census.columns.age, func.sum(census.columns.pop2008)])
stmt = stmt.group_by(census.columns.sex, census.columns.age)
result = connection.execute(stmt).fetchall()

print(result)