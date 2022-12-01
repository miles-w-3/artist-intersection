from flask import Blueprint
from src.util import Util

# Create a new blueprint for managers
admin = Blueprint('admin', __name__)


@admin.route('/admins')
def get_all_admins():
    return Util.query_db('SELECT * FROM Admin')


@admin.route('/admins/<admin_id>')
def get_admin_by_id(admin_id):
    return Util.query_db(f'SELECT * FROM Admin WHERE admin_id={admin_id}')


@admin.route('/suspended')
def get_all_suspended():
    return Util.query_db(f'SELECT * FROM Suspended')
