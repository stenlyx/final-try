from typing import List

from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)
    amount = db.Column(db.Integer, default=1)
    size = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    material = db.Column(db.String(80), nullable=False)
    _print = db.Column(db.Boolean, default=False)
    color = db.Column(db.String(80), nullable=False)
    new = db.Column(db.Boolean, default=False)
    bestseller = db.Column(db.Boolean, default=False)
    sale = db.Column(db.Boolean, default=False)

    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.all()

    @classmethod
    def find_all_by_brand(cls, brand: str) -> List["ItemModel"]:
        return cls.query.filter_by(brand=brand).all()

    @classmethod
    def find_if_new(cls, new=True):
        return cls.query.filter_by(new=new).all()

    @classmethod
    def find_if_bestseller(cls, bestseller=True):
        return cls.query.filter_by(bestseller=bestseller).all()

    @classmethod
    def on_sale(cls, sale=True):
        return cls.query.filter_by(sale=sale).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
