from flask import Blueprint, jsonify, request
from werkzeug import secure_filename
import os
from model import Package


api = Blueprint('api', __name__)

UPLOAD_FOLDER = '/home/jason/apm_uploads'


@api.route('/list_packages')
def list_packages():
    packs = Package.query.all()
    return jsonify(packs_available = packs)

@api.route('/upload_package', methods = ['GET', 'POST'])
def upload_package():
    if request.method == 'POST':
       file = request.files['file']
       if file:
           filename = secure_filename(file.filename)
           file.save(os.path.join(UPLOAD_FOLDER, filename))
           return 'OK'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
 
