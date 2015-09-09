from flask import Blueprint, jsonify
from model import Package

api = Blueprint('api', __name__)

@api.route('/list_packages')
def list_packages():
    packs = Package.query.all()
    return jsonify(packs_available = packs)

