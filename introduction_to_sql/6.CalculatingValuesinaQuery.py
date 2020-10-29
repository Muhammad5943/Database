from sqlalchemy import create_engine, Table, MetaData, select, func, desc
from sqlalchemy import case
from sqlalchemy import cast, Float

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload = True, autoload_with = engine)

# logic format1
""" stmt = select([census.columns.age, (census.columns.pop2008 - census.columns.pop2000).label('pop_change')])
stmt = stmt.group_by(census.columns.age)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(5)
"""
# result
""" results = connection.execute(stmt).fetchall()
print(results) """

# logic format2
""" stmt = select([census.columns.age, (census.columns.pop2008 - census.columns.pop2000).label('pop_change')])
stmt = stmt.group_by(census.columns.age)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(5)
stmt = select([
    func.sum(
        case([(
            census.columns.state == "New York",
            census.columns.pop2008
        )], else_ = 0)
    )
])
# result
results = connection.execute(stmt).fetchall()
print(results) """

# logic format3
stmt = select([census.columns.age, (census.columns.pop2008 - census.columns.pop2000).label('pop_change')])
stmt = stmt.group_by(census.columns.age)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(5)
stmt = select([
    (func.sum(
        case([
            (   census.columns.state == 'New York',
                census.columns.pop2008)
            ], else_ = 0)) / 
        cast(
            func.sum(census.columns.pop2008),
            Float) * 100).label('NewYork%')
])
# result
results = connection.execute(stmt).fetchall()
print(results)