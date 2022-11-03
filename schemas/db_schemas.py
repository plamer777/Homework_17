"""This unit contains schemas for serializing and deserializing database's
models"""
from marshmallow import Schema, fields
# -----------------------------------------------------------------------


class MovieSchema(Schema):
    """The schema for a Movie class model"""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class DirectorSchema(Schema):
    """The schema for a Director class model"""
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    """The schema for a Genre class model"""
    id = fields.Int()
    name = fields.Str()
