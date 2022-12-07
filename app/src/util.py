from flask import Flask, jsonify
from flaskext.mysql import MySQL

class Util:

    logged_in_id = 2
    db_connection = None
    #cursor = None

    @classmethod
    def init_db(cls, db_connection: MySQL):
        print(f"db connection is {db_connection}")
        cls.db_connection = db_connection
        print(f"cls db is  {cls.db_connection}, then {cls.db_connection.get_db()}")

        #cls.cursor =  cls.db_connection.get_db().cursor()

    @classmethod
    def query_db(cls, query):
        json_data = cls.query_db_json(query)
        return jsonify(json_data)

    @classmethod
    # get the json object before wrapping
    def query_db_json(cls, query):
        db = cls.db_connection.get_db()
        cur = db.cursor()
        cur.execute(query)
        row_headers = [x[0] for x in cur.description]
        json_data = []
        theData = cur.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        return json_data

    @classmethod
    def insert_db(cls, statement):
        db = cls.db_connection.get_db()
        cur = db.cursor()
        try:
            cur.execute(statement)
        except Exception as e:
            cls.log(f"Failed to insert to db {str(e)}")
            return False
        else:
            db.commit()
            return True

    @classmethod
    def log(cls, msg):
        print(msg, flush=True)


