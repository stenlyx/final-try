from typing import List
import datetime
from sqlalchemy import func

from db import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(1000), nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=func.now())

    @classmethod
    def find_by_name(cls, name: str) -> "PostModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["PostModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
