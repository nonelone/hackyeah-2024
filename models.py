from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import select, insert
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, text

#engine definition.
engine = create_engine("sqlite+pysqlite:///urls.db", echo=True)

class Base(DeclarativeBase):
    pass


class Service(Base):
    __tablename__ = "service"

    id: Mapped[int] = mapped_column(primary_key=True) #todo
    name = mapped_column(String(100), unique=True) #todo
    description = mapped_column(String(10)) #todo


    def __repr__(self) -> str:
        return f"Service(name={self.name!r}, id={self.id!r})"


class Url(Base):
    __tablename__ = "url_string"

    url_id: Mapped[int] = mapped_column(String(512), primary_key=True) #todo
    service_id = mapped_column(ForeignKey("service.id"))

    def __repr__(self) -> str:
        return f"Url(url_id={self.url_id!r}, service_id={self.service_id!r})"


#Create models.
Base.metadata.create_all(engine)

def execute_and_print_query(query):
    with engine.connect() as conn:
        for row in conn.execute(query):
            print(row)
        conn.commit()

def execute_query(query):
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()

def print_services():
    stmt = select(Service)
    print(stmt)
    execute_and_print_query(stmt)

def print_urls():
    stmt = select(Url)
    print(stmt)
    execute_and_print_query(stmt)

def insert_service(name : str, description : str ):
    """Returns primary key of an inserted service."""
    stmt = insert(Service).values(name=name, description=description).prefix_with('OR IGNORE')
    with engine.connect() as conn:
        conn.execute(stmt)
        cursor = conn.execute(text("SELECT last_insert_rowid()"))
        key = cursor.first()[0] #Get service's id from cursor object.
        print(key)
        conn.commit()

        return key #Return id of an inserted service.

def insert_url(url : str, service_id: int):
    stmt = insert(Url).values(url_id=url, service_id=service_id).prefix_with('OR IGNORE')
    print(stmt)
    execute_query(stmt)

def select_urls_for_service(service_id: int):
    stmt = select(Url).where(Url.service_id == service_id)
    execute_and_print_query(stmt)
