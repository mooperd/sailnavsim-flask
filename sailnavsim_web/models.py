"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Boat(db.Model):
    __tablename__   = 'Boat'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.Text, nullable=False, unique=True)
    race            = db.Column(db.Text, nullable=False)
    desiredCourse   = db.Column(db.Float, nullable=False)
    started         = db.Column(db.Integer, nullable=False)
    boatType        = db.Column(db.Integer, nullable=False)
    isActive        = db.Column(db.Integer, nullable=False)
    boatFlags       = db.Column(db.Integer, nullable=False)
    race            = db.relation("BoatRace", backref="Boat")
    race_id         = db.Column(db.Integer, db.ForeignKey('BoatRace.id'))
    user            = db.relation("User", backref="User")
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'))


class BoatRace(db.Model):
    __tablename__   = 'BoatRace'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String, nullable=False, unique=True)
    latitude        = db.Column(db.Float, nullable=False)
    longitude       = db.Column(db.Float, nullable=False)
    sw_corner       = db.Column(db.Float, nullable=False)
    ne_corner       = db.Column(db.Float, nullable=False)
    boat_type       = db.Column(db.Integer, nullable=False)
    start_time      = db.Column(db.Integer, nullable=False)
    private         = db.Column(db.Integer, nullable=False)


class BoatLog(db.Model):
    __tablename__   = 'BoatLog'
    __table_args__ = (
        db.UniqueConstraint('boat_id', 'time', name='unique_boat_id_time'),
    )
    time            = db.Column(db.Integer, nullable=False)
    lat             = db.Column(db.Float, nullable=False)
    lon             = db.Column(db.Float, nullable=False)
    courseWater     = db.Column(db.Float, nullable=False)
    speedWater      = db.Column(db.Float, nullable=False)
    trackGround     = db.Column(db.Float, nullable=False)
    speedGround     = db.Column(db.Float, nullable=False)
    windDir         = db.Column(db.Float, nullable=False)
    windSpeed       = db.Column(db.Float, nullable=False)
    oceanCurrentDir = db.Column(db.Float)
    oceanCurrentSpeed = db.Column(db.Float)
    waterTemp       = db.Column(db.Float)
    temp            = db.Column(db.Float, nullable=False)
    dewpoint        = db.Column(db.Float, nullable=False)
    pressure        = db.Column(db.Float, nullable=False)
    cloud           = db.Column(db.Integer, nullable=False)
    visibility      = db.Column(db.Integer, nullable=False)
    precipRate      = db.Column(db.Float, nullable=False)
    precipType      = db.Column(db.Integer, nullable=False)
    boatStatus      = db.Column(db.Integer, nullable=False)
    boatLocation    = db.Column(db.Integer, nullable=False)
    waterSalinity   = db.Column(db.Float)
    oceanIce        = db.Column(db.Integer)
    distanceTravelled = db.Column(db.Float, nullable=False)
    damage          = db.Column(db.Float, nullable=False)
    windGust        = db.Column(db.Float, nullable=False)
    waveHeight      = db.Column(db.Float)
    compassMagDec   = db.Column(db.Float, nullable=False)
    invisibleLog    = db.Column(db.Integer, nullable=False)
    boat            = db.relation("Boat", backref="Boat")
    boat_id         = db.Column(db.Integer, db.ForeignKey('Boat.id'))

    __mapper_args__ = {
        "primary_key": [boat_id, time]
    }


class MyIP(db.Model):
    """Some IP Addresses"""
    __tablename__   = 'ip_addresses'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String, nullable=False)
    ip              = db.Column(db.String, nullable=False)
    user            = db.relation("User", backref="Users")
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'))