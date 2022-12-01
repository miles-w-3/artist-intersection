from flask import Flask, jsonify
from flaskext.mysql import MySQL

class Util:

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
        cur = cls.db_connection.get_db().cursor()
        cur.execute(query)
        row_headers = [x[0] for x in cur.description]
        json_data = []
        theData = cur.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        return jsonify(json_data)


