from flask import Flask, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

class User(Resource):
    """This class will define methods for the user"""
    def post(self):
        """This class creates a user"""
        pass

    def get(self, id):
        """This method gets the details of a user"""
        pass

    def put(self, id):
        """This method modifies the details of a user"""
        pass

    def delete(self, id):
        """This method deletes a user"""
        pass

api.add_resource(User, 'api/v1/user-dashboard/<int:id>', endpoint = 'user')

reqests = [
    {
        "id": "0",
        "category": "maintenance",
        "title": "fogort password",
        "frequency": "once",
        "description": "i am stupid",
        "status": "Pending"
    },
    {
        "id": "1",
        "category": "repair",
        "title": "fogort hammer",
        "frequency": "once",
        "description": "i am also stupid",
        "status": "Pending"
    },
    {
        "id": "2",
        "category": "maintenance",
        "title": "Tissue out",
        "frequency": "daily",
        "description": "well, not cool",
        "status": "Pending"
    }
]

request_fields = {
    'category': fields.String,
    'title':fields.String,
    'frequence':fields.String,
    'description':fields.String,
    'status':fields.String,
    'uri': fields.Url('request')
}  

class RequestList(Resource):
    """Holds methods for giving all requests"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('category', type=str, required=True,
                                   help='No task category provided',
                                   location='json')
        self.reqparse.add_argument('frequency', type=str, required=True,
                                   help='No task frequency provided',
                                   location='json')
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, required=True,
                                   help='No task description provided',
                                   location='json')
        self.reqparse.add_argument('status', type=str,
                                   default= "Pending",
                                   location='json')
        super(RequestList, self).__init__()
        
