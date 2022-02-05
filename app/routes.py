from flask import jsonify, request
from app import api,db
from flask_restx import Resource
from app.apimodels import dataset_model
from app.models import Dataset


@api.route('/datasets')
class Datasets(Resource):
    @api.marshal_list_with(dataset_model,code=200,envelope='datasets')
    def get(self):
        '''
        Get all datasets'''
        datasets = Dataset.query.all()
        return datasets
    
    @api.marshal_with(dataset_model,code=201,envelope='dataset')
    @api.doc(params={'isim':'Dataset name','dosya_adi':'Dataset file name','dosya_yolu':'Dataset file path','kullanici_id':'Dataset user id'})
    def post(self):
        '''
        Create a new dataset'''
        json_data = request.get_json()
        isim = json_data.get('isim')
        dosya_adi = json_data.get('dosya_adi')
        dosya_yolu = json_data.get('dosya_yolu')
        kullanici_id = json_data.get('kullanici_id')
        new_dataset = Dataset(isim=isim,dosya_adi=dosya_adi,dosya_yolu=dosya_yolu,kullanici_id=kullanici_id)
        db.session.add(new_dataset)
        db.session.commit()
        return new_dataset

@api.route('/datasets/<int:id>')
class DatasetItem(Resource):
    @api.marshal_with(dataset_model,code=200,envelope='dataset')
    def get(self, id):
        '''
        Get a dataset by id'''
        dataset = Dataset.query.get_or_404(id)
        return dataset
    

    
    @api.marshal_with(dataset_model,code=200,envelope='dataset')
    def delete(self, id):
        '''
        Delete a dataset by id'''
        dataset = Dataset.query.get_or_404(id)
        db.session.delete(dataset)
        db.session.commit()
        return dataset,200
        

    @api.marshal_with(dataset_model,code=200,envelope='dataset')
    def put(self, id):
        '''
        Update a dataset by id'''
        dataset_to_update = Dataset.query.get_or_404(id)
        json_data = request.get_json(force=True)
        dataset_to_update.isim = json_data.get('isim')
        dataset_to_update.dosya_adi = json_data.get('dosya_adi')
        dataset_to_update.dosya_yolu = json_data.get('dosya_yolu')
        dataset_to_update.kullanici_id = json_data.get('kullanici_id')
        db.session.commit()
        return dataset_to_update
