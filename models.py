from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import os

class Base(DeclarativeBase): pass

db = SQLAlchemy(model_class=Base)

class Service(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class ServiceUrl(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(unique=True)

class SuspiciousUrl(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(unique=True)
    evil_factor: Mapped[int] = mapped_column()

#service_table = db.Table(
#    sa.Column("provider_id", sa.ForeignKey(Service.id), primary_key=True),
#    sa.Column("url_id", sa.ForeignKey(ServiceUrl.id), primary_key=True),
#)


def report_url(url):
    if db.session.query(SuspiciousUrl).filter_by(url = url).first() is not None:
        db.session.query(SuspiciousUrl).filter_by(url = url).update({'evil_factor': SuspiciousUrl.evil_factor + 1})
    else:
        evil_url = SuspiciousUrl(url=url, evil_factor=1)
        db.session.add(evil_url)
    db.session.commit()

def init_database():
    if os.path.isfile('instance/db'): print("Database found")
    else: 
        db.create_all()
        print("Created new database")
