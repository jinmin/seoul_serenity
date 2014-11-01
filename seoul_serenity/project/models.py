# -*- coding: utf-8 -*-
import datetime as dt

from flask.ext.login import UserMixin

from seoul_serenity.extensions import bcrypt
from seoul_serenity.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

# Project
class Project(SurrogatePK, Model):
    __tablename__ = 'projects'
    name = Column(db.String(80), unique=False, nullable=False)
    start_date = Column(db.DateTime, nullable=True)
    end_date = Column(db.DateTime, nullable=True)
    # minwook
    # description = Column(db.Text, nullable=True)
    # created_u_id = Column(db.Integer, nullable=False)
    # modified_at = Column(db.DateTime, nullable=True)
    # modified_u_id = Column(db.Integer, nullable=True)
    # display_yn = Column(db.Boolean, default=True)

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        return '<Project({name})>'.format(name=self.name)

# Project Iteration
class ProjectIteration(SurrogatePK, Model):
    __tablename__ = 'protject_iteration'
    p_id = Column(db.Integer)
    v_id = Column(db.Integer)
    week = Column(db.Integer)
    created_at = Column(db.DateTime, nullable=False)
    


