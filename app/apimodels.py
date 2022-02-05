from flask_restx import fields 
from app import api 

dataset_model = api.model('Dataset', 
{'id':fields.Integer(),
'isim':fields.String(),
'dosya_adi':fields.String(),
'dosya_yolu':fields.String()})
