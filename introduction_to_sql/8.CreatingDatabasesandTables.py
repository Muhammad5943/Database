from sqlalchemy import create_engine, MetaData
from sqlalchemy import ( Table, Column, String, Integer, Float, Boolean, func, select )

# inserting data tu the table
from sqlalchemy import insert

# updating data in the table
from sqlalchemy import update

# updating data with desc
from sqlalchemy import desc

# deleting data from table and delete table
from sqlalchemy import delete

engine = create_engine('sqlite:///employees.sqlite')
connection = engine.connect()
metadata = MetaData()

#TODO: dasar pembuatan fatabse dan table pada datascience python
""" employees = Table('employees', metadata, 
        Column('id', Integer()),
        Column('name', String(255)),
        Column('salary', Float()),
        Column('active', Boolean())
)

metadata.create_all(engine)
engine.table_names() """

#TODO: membuat database dan table menggunakan nilai default
employees = Table('employees', metadata,
    Column('id', Integer()),
    Column('name', String(255), unique = False, nullable = True),
    Column('salary', Float(), default = 100.00),
    Column('active', Boolean(), default = True)
)

# print(*employees.constraints, sep='\n')

""" metadata.create_all(engine)
engine.table_names() """

#TODO: inserting data in the table
""" employees = Table('employees', metadata, autoload = True, autoload_with = engine)
stmt = insert(employees).values(id = 1, name = "Jason", salary = 1.00, active = True)

result = connection.execute(stmt)
print(result.rowcount) """

# Inserting multiple data to database
""" stmt = insert(employees)
values_list = [
    {'id':2, 'name': 'Rebecca', 'salary': 2.00, 'active': True},
    {'id':3, 'name': 'Bob', 'salary': 0.00, 'active': False}
]

result = connection.execute(stmt, values_list)
print(result.rowcount) """

# To show inserting data to the database
""" stmt = select([employees])
result = connection.execute(stmt).fetchall()

print(*result, sep = '\n') """

#TODO:  Update data in the database
""" stmt = update(employees)
stmt = stmt.where(employees.columns.id == 3)
stmt = stmt.values(active = True)

result = connection.execute(stmt)
print(result.rowcount)

stmt = select([employees])
result = connection.execute(stmt).fetchall()

print(*result, sep = '\n') """

# update multiple data in database
""" stmt = update(employees)
stmt = stmt.where(employees.columns.active == True)
stmt = stmt.values(active = False, salary = 0.00)
result = connection.execute(stmt)
# print(result.rowcount)

stmt = select([employees])
results = connection.execute(stmt).fetchall()
print(*results, sep = '\n') """

# Corelated update (digunakan untuk mengubah record yang bernilai max/ mengubah string agar cocok dengan table lain)
""" new_salary = select([employees.columns.salary])
new_salary = new_salary.order_by(desc(employees.columns.salary))
new_salary = new_salary.limit(1)
print(new_salary)

stmt = update(employees)
stmt = stmt.values(salary = new_salary)
results = connection.execute(stmt)

print(results.rowcount)

stmt = select([employees])
result = connection.execute(stmt).fetchall()

print(*result, sep = '\n') """

# Displaying data in table
""" stmt = select([employees])
result = connection.execute(stmt).fetchall()
print(*result, sep = '\n') """

# TODO: Deleting table and database
""" stmt = delete(employees).where(employees.columns.id == 3)
results = connection.execute(stmt)
print(results.rowcount) """

# to counting the data that exists in database
""" stmt = select([func.count(employees.columns.id)])
results = connection.execute(stmt).scalar()
print(results, '\n') """

# delete all table data in the database
""" delete_stmt = delete(employees)
results = connection.execute(delete_stmt)
print(results.rowcount) """

# Drop single table from database
""" employees.drop(engine)
print(employees.exists(engine)) """

# Drop All Table in Database
metadata.drop_all(engine)

# to display the table list
print(engine.table_names())
