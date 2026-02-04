from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///maindb.db", echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    
    things = relationship("Thing", back_populates="person")

class Thing(Base):
    __tablename__ = "things"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner_id = Column(Integer, ForeignKey("people.id"))
    
    person = relationship("Person", back_populates="things")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_person = Person(name="Tom", age=58)
# session.add(new_person)

# new_person = Person(name="Charlie", age=64)
# session.add(new_person)
# session.flush()  # to get the id of new_person before committing

# new_thing = Thing(description='Camera', value=500, owner_id=new_person.id)
# session.add(new_thing)

# session.commit()

# print([t.description for t in new_person.things])
# print(new_thing.person.name)

# result = session.query(Person.name, Person.age).all()
# print(result)

# result = session.query(Person).filter(Person.age > 50).all()
# print([p.name for p in result])

# result = session.query(Thing).filter(Thing.value < 50).delete()
# session.commit()

# result = session.query(Thing).filter(Thing.value < 50).all()
# print([t.description for t in result])

# result = session.query(Person).filter(Person.name == "Charlie").update({"name": "Charles"})
# session.commit()

# result = session.query(Person.name).all()
# print(result)

# result = session.query(Person.name, Thing.description).join(Thing).all()
# print(result)

# result = session.query(Thing.owner_id, func.sum(Thing.value)).group_by(Thing.owner_id).all()
# print(result)

# result = session.query(Thing.owner_id, func.sum(Thing.value)).group_by(Thing.owner_id).having(func.sum(Thing.value) > 100).all()
# print(result)

session.close()
# closes the connection and commit anything if not commited
