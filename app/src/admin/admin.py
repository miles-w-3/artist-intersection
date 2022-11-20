from flask import Blueprint

# Create a new blueprint for managers
admin = Blueprint('admin', __name__)

# add a route to this blueprint
@admin.route('/admins')
def get_all_managers():
    return f'<h1>Getting all the collectors.</h1>'
