from flask import Blueprint, request, Response, jsonify
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

@artist.route('artist/works/<artist_id>')
def get_works_by_artist(artist_id):
    Util.log(f"HERE, id {artist_id}")
    query = "SELECT title, date_created, current_price, type_name AS genre, name AS purchased_by " \
        f"FROM (Work w JOIN WorkType wt on w.work_type_id = wt.type_id) LEFT JOIN Collector c ON purchased_by_id = c.collector_id WHERE creator_id={artist_id};"
    return Util.query_db(query)

@artist.route('/types')
def get_all_types():
    query = "SELECT type_name AS label, type_id AS value FROM WorkType;"
    return Util.query_db(query)

@artist.route('/works')
def get_all_works():
    query = "SELECT * FROM Work;"
    return Util.query_db(query)

@artist.route('/works/<work_id>', methods = ['GET', 'POST'])
def get_work_by_id(work_id):
    if request.method == 'GET':
        query = f"SELECT * FROM Work WHERE work_id={work_id};"
        return Util.query_db(query)
    elif request.method == 'POST':
        title = request.form['title']
        price = float(request.form['price'])
        workType = int(request.form['workType'])
        logged_in = int(request.form['login'])
        if work_id == 'create':
            insert = "INSERT INTO Work (title, work_type_id, creator_id, current_price) " \
                    f"VALUES ('{title}', {workType}, {logged_in}, {price});"
            if Util.insert_db(insert):
                return Response(status=200)
            return Response(status=403)


@artist.route('/names')
def get_artist_select():
    query = "SELECT artist_id AS value, name AS label " \
            "FROM Artist;"
    return Util.query_db(query)
