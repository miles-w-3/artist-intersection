from flask import Blueprint

artist = Blueprint('artist', __name__)

@artist.route('/artists')
def get_all_customers():
    return f'<h1>Getting all the artists from {__file__} file.</h1>'
