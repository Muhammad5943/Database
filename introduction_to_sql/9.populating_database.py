from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select, func
import csv
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///demography.sqlite')
connection = engine.connect()
metadata = MetaData()
demography = Table('demography', metadata,
        Column('kode_bps', Integer(), primary_key = True),
        Column('nama', String(255), nullable = False),
        Column('ibukota', String(255), nullable = False),
        Column('populasi', String(255)),
        Column('luas', String(255)),
        Column('pulau', String(255), nullable = False)
)

# created database with this code
""" metadata.create_all(engine) """
demography = Table('demography', metadata, autoload = True, autoload_with = engine)

# print(engine.table_names())

values_list = []
with open('demography.csv') as data:
    next(data)
    reader = csv.reader(data)
    for row in reader:
        data = {'kode_bps': row[0], 'nama': row[1], 'ibukota': row[2], 'populasi': row[3], 'luas': row[4], 'pulau': row[5]}
        values_list.append(data)

# print(*values_list, sep = '\n')

# inserting data in database with this code
""" stmt = insert(demography)
results = connection.execute(stmt, values_list)

print(results.rowcount) """

stmt = select([demography])
result = connection.execute(stmt).fetchall()

# print(*result, sep = '\n')

stmt = select([demography.columns.pulau, func.sum(func.replace(demography.columns.populasi,'.','')).label('populasi')])
stmt = stmt.group_by(demography.columns.pulau)
stmt = stmt.order_by(demography.columns.pulau)
results = connection.execute(stmt).fetchall()

# print(*results, sep = '\n')

df = pd.DataFrame(results)
df.columns = results[0].keys()

# print(df)

df.plot(kind = 'bar', x = 'pulau', y = 'populasi')
plt.xlabel('Pulau')
plt.xlabel('Populasi')
plt.title('Total Populasi di Indonesia')
plt.show()