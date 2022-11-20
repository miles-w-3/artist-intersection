from flask import Blueprint

# Create a new blueprint for managers
collector= Blueprint('collector', __name__)

# add a route to this blueprint
@collector.route('/collectors')
def get_all_managers():
    return f'<h1>Getting all the collectors.</h1>'
