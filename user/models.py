from flask import Flask, jsonify

class User:
    
    #each method on a class in python needs the instance of the class passed in as the first parameter. hence the use of 'self'
    def signup(self):
        
        user = {
            
            # ID is listed as _id becuase thats how it is stored in MongoDb
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }
        
        # we want this to come back in a JSON format so we will use JSONIFY. This is a flask func, so we will import from flask
        #if succesful we can return status code of 200. Replace '200' with '400' for failed statud calls.
        return jsonify(user), 200
    
    