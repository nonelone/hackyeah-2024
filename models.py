from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import Levenshtein

import os, codecs

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

def verify_url(url):
    url = url.replace("https://","")
    clear = url.decode("utf-8")
    url = clear.encode("ascii","ignore")
    vile_shit = ServiceUrl.query.all()
    results = []
    for contested_url in vile_shit:
        contested_url = (contested_url.url).replace("\n","")
        distance = Levenshtein.distance(url, contested_url)
        if distance < 2 and distance != 0:
            results.append(f"{contested_url} @ {distance}")
            return False
    return True

def import_websites_from_csv(path):
    with open(path) as file:
        while line := file.readline():
            new_url = ServiceUrl(url=line)
            db.session.add(new_url)

    db.session.commit()

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
        import_websites_from_csv("cloudflare-radar_top-1000-domains_20240916-20240923.csv")
        print("Created new database")
