from flask import Blueprint
from src.util import Util

artist = Blueprint('artist', __name__)

@artist.route('/artists')
def get_all_artists():
    query = "SELECT artist_id AS id, name, date_of_birth as dob, num_works_sold AS works_sold," \
            " total_commission_amt AS total_commission, location AS city, type_name AS favorite_genre" \
            " FROM Artist A JOIN WorkType WT on A.favorite_works_id = WT.type_id;"
    return Util.query_db(query)

@artist.route('/artist_id/<artist_id>')
def get_artist_by_id(artist_id):
    query = "SELECT artist_id AS id, name, date_of_birth as dob, num_works_sold AS works_sold," \
            " total_commission_amt AS total_commission, location AS city, type_name AS favorite_genre" \
           f" FROM Artist A JOIN WorkType WT on A.favorite_works_id = WT.type_id WHERE artist_id={artist_id};"
    return Util.query_db(query)

@artist.route('/types')
def get_all_types():
    query = "SELECT type_name AS label, type_id AS value FROM WorkType;"
    return Util.query_db(query)

@artist.route('/works')
def get_all_works():
    query = "SELECT * FROM Work;"
    return Util.query_db(query)

@artist.route('/work_id/<work_id>')
def get_work_by_id(work_id):
    query = f"SELECT * FROM Work WHERE work_id={work_id};"
    return Util.query_db(query)
