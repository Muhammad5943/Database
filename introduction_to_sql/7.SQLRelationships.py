from sqlalchemy import create_engine, MetaData, Table, select, func, case, cast
from sqlalchemy import MetaData, Table, select, func
from sqlalchemy import join

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload = True, autoload_with = engine)
state_fact = Table('state_fact', metadata, autoload = True, autoload_with = engine)
stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])
results = connection.execute(stmt).fetchall()
# print(results)

# view lebih rapi
# print(*results, sep='\n')

stmt = select([func.sum(census.columns.pop2008)])
stmt = stmt.select_from(census.join(state_fact, state_fact.columns.name == census.columns.state))

# to knot the relqtion code
print(stmt)

stmt = stmt.where(state_fact.columns.circuit_court == '10')
results = connection.execute(stmt).scalar()
print(results)