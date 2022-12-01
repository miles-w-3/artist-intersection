from flask import Blueprint
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

@collector.route('/collectors/<collector_id>')
def get_collector_by_id(collector_id):
    query = "SELECT collector_id AS id, name, date_of_birth AS dob, " \
            "num_works_purchased AS works_purchased, total_spend_amt, " \
            "type_name AS favorite_genre FROM Collector c JOIN WorkType WT " \
            f"on c.favorite_works_id = WT.type_id WHERE collector_id={collector_id};"
    return Util.query_db(query)

@collector.route('/requests')
def get_all_requests():
    query = "SELECT * FROM CommissionRequest;"
    return Util.query_db(query)

@collector.route('/requests/<request_id>')
def get_work_by_id(request_id):
    query = f"SELECT * FROM CommissionRequest WHERE request_id={request_id};"
    return Util.query_db(query)

