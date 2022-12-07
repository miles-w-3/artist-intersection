from flask import Blueprint, request, Response
from src.util import Util

# Create a new blueprint for managers
admin = Blueprint('admin', __name__)


@admin.route('/admins')
def get_all_admins():
    return Util.query_db('SELECT name as label, admin_id as value FROM Admin;')


@admin.route('/admins/<admin_id>')
def get_admin_by_id(admin_id):
    return Util.query_db(f'SELECT * FROM Admin WHERE admin_id={admin_id};')


@admin.route('/suspended')
def get_all_suspended():
    return Util.query_db(f'SELECT * FROM SuspendedArtist;')


@admin.route('/suspended/<artist_id>', methods=['GET', 'POST'])
def get_suspended_artist(artist_id):
    if request.method == 'GET':
        return Util.query_db(f'SELECT * FROM SuspendedArtist WHERE suspended_id = {artist_id};')

    if request.method == 'POST':
        suspended_by = int(request.form['admin_id'])
        reason = request.form['reason']
        suspended = int(artist_id)
        insert = "INSERT INTO SuspendedArtist (suspended_id, suspended_by, reason) " \
            f"VALUES ({suspended}, {suspended_by}, '{reason}');"
        if Util.insert_db(insert):
            return Response(status=200)
        return Response(status=403)
