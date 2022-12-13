from flask import Blueprint, Response, request
from src.util import Util
# Create a new blueprint for managers
collector= Blueprint('collector', __name__)

# add a route to this blueprint
@collector.route('/collectors')
def get_all_collectors():
    query = "SELECT collector_id AS id, name, date_of_birth AS dob, " \
            "num_works_purchased AS works_purchased, total_spend_amt, " \
            "type_name AS favorite_genre FROM Collector c JOIN WorkType WT " \
            "on c.favorite_works_id = WT.type_id;"
    return Util.query_db(query)

# add a route to this blueprint
@collector.route('/names')
def get_collector_select():
    query = "SELECT collector_id AS value, name AS label " \
            "FROM Collector;"
    return Util.query_db(query)

@collector.route('/collectors/<collector_id>')
def get_collector_by_id(collector_id):
    query = "SELECT collector_id AS id, name, date_of_birth AS dob, " \
            "num_works_purchased AS works_purchased, total_spend_amt, " \
            "type_name AS favorite_genre FROM Collector c JOIN WorkType WT " \
            f"on c.favorite_works_id = WT.type_id WHERE collector_id={collector_id};"
    return Util.query_db(query)

@collector.route('/requests/collector/<collector_id>')
def get_works_by_collector(collector_id):
    query = "SELECT title, info, type_name AS genre, name AS accepted_by " \
            "FROM (CommissionRequest c JOIN WorkType wt ON c.work_type_id = wt.type_id) " \
            f"LEFT JOIN Artist a ON accepted_id = a.artist_id WHERE requestor={collector_id};"
    return Util.query_db(query)

@collector.route('/requests')
def get_all_requests():
    query = "SELECT * FROM CommissionRequest;"
    return Util.query_db(query)

@collector.route('/request/<request_id>', methods = ['GET', 'POST'])
def manage_work_requests(request_id):
    Util.log(f"In route message, request is {repr(request_id)}, method is {repr(request.method)}")
    # handle gets
    if request.method == 'GET':
        id = int(id)
        query = f"SELECT * FROM CommissionRequest WHERE request_id={id};"
        return Util.query_db(query)
    elif request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        workType = int(request.form['workType'])
        logged_in = int(request.form['cltr'])

        #Util.log(f"In post block {repr(request_id)} | bool is {request_id == 'create'}")
        #Util.log(f"Got POST: {request.form}")
        # for creating a new request
        if request_id == 'create':
            Util.log(f"Three: {title}, {desc}, {workType}")
            insert = "INSERT INTO CommissionRequest (title, info, work_type_id, requestor) " \
                     f"VALUES ('{title}', '{desc}', {workType}, {logged_in});"
            Util.log(f"Request IS {insert}")
            if Util.insert_db(insert):
                return Response(status=200)
            # return 403 if the post didn't work
            return Response(status=403)
            #result = Util.query_db(insert)
            #Util.log(f"Result is: {result}")
        elif request_id != 'create':
            Util.log("didn't get in")
        Util.log(f"After post block {repr(request_id)} | bool is {request_id == 'create'}")

# @collector.route('/requests/create', methods = ['POST'])
# def create_work_request():
#     print(f"Got POST: {request.json}")


#{{artistSelect.data.splice(0)}}

#[{{artistProfile.data.find(element => element.id == appsmith.store.selectArtist)}}]
