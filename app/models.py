from app import db
from datetime import datetime,timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import os

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    token = db.Column(db.String(32))
    token_expiration = db.Column(db.DateTime)
    kullanici = db.relationship('Dataset', backref='dataset',lazy='dynamic')
    def set_password(self, sifre):
        self.sifre_hash = generate_password_hash(sifre)
    
    def check_password(self, sifre):
        return check_password_hash(self.sifre_hash, sifre)

    def get_token(self,expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        kullanici = Users.query.filter_by(token=token).first()
        if kullanici is None or kullanici.token_expiration < datetime.utcnow():
            return None
        return kullanici
        
    def __repr__(self):
        return '<Kullanici {}>'.format(self.kullanici_adi)



class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(64), index=True, unique=True)
    dosya_adi = db.Column(db.String(64), index=True, unique=True)
    dosya_yolu = db.Column(db.String(128), index=True, unique=True)
    kullanici_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return '<Datasets {}>'.format(self.isim)