# This is all just the basic syntax based code for the sqlalchemy which we genrally do not use
'''
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///mydb.db", echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR)"))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)

session.execute(text('INSERT INTO users (name, id) VALUES ("Ayush", 1)'))

session.commit()
'''

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, func, insert, Float, ForeignKey

engine = create_engine("sqlite:///mydb.db", echo=True)
# engine = create_engine("postgresql+psycopg2://user_name:password@localhost:5432/database_name", echo=True)

meta = MetaData()

people = Table(
    "people", 
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer)
)

things = Table(
    "things",
    meta,
    Column("id", Integer, primary_key=True),
    Column("description", String, nullable=False),
    Column("value", Float),
    Column("owner_id", Integer, ForeignKey("people.id"))
)

meta.create_all(engine)

conn = engine.connect()


## How to insert

# insert_statement = people.insert().values(id=1, name="John Doe", age=30) # here if we do not provide id it will automatically increment
# # insert = insert(people).values(id=1, name="John Doe", age=30)) alternate method for which we have to import insert from sqlalchemy
# result = conn.execute(insert_statement)
# conn.commit()
# if you insert the same value again it will give an error because of primary key constraint


## How to select

# select_statement = people.select().where(people.c.age > 25)
# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)


## How to update

# update_statement = people.update().where(people.c.name == "John Doe").values(age=50)
# result = conn.execute(update_statement)
# conn.commit()


## How to delete

# delete_statement = people.delete().where(people.c.name == "John Doe")
# result = conn.execute(delete_statement)
# conn.commit()


insert_people = people.insert().values([
    {"name": "Ayush", "age": 22},
    {"name": "Aditya", "age": 22},
    {"name": "Kapi", "age": 22},
    {"name": "Abhi", "age": 22},
    {"name": "Akshat", "age": 22}
])

inser_things = things.insert().values([
    {"owner_id": 2, "description": "Laptop", "value": 800.50},
    {"owner_id": 2, "description": "Mouse", "value": 50.50},
    {"owner_id": 2, "description": "Keyboard", "value": 100.50},
    {"owner_id": 3, "description": "Book", "value": 20},
    {"owner_id": 4, "description": "Lamp", "value": 60.75},
    {"owner_id": 5, "description": "Buds", "value": 80.50},
])

# conn.execute(insert_people)
# conn.commit()

# conn.execute(inser_things)
# conn.commit()


## How to join tables

# join_statement = people.join(things, people.c.id == things.c.owner_id)  # only join means inner join
# # join_statement = people.outerjoin(things, people.c.id == things.c.owner_id)  # outer join gives data for everyone even if they don't own anything
# select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement)

# result = conn.execute(select_statement)
# for row in result.fetchall():
#     print(row)


## How to implement group by logic

# # group_by_statement = things.select().with_only_columns(things.c.owner_id, func.sum(things.c.value)).group_by(things.c.owner_id)
# group_by_statement = things.select().with_only_columns(things.c.owner_id, func.sum(things.c.value)).group_by(things.c.owner_id).having(func.sum(things.c.value) > 70)
# result = conn.execute(group_by_statement)

# for row in result.fetchall():
#     print(row)


