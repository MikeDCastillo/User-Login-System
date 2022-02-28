# This file will contain all the routes pertaining to the user such as 'user/signup' or 'user/login'
# In order to create routes, we need the app instance. in this case from the file 'app.py'

from flask import Flask
# from the app file or module, then import that instance of the Flask in that file.
from app import app
## we want the signup method on the User class. So we need to reference the file and then import the class to have that method
## we reference the folder User, then call down to the models file with dot syntax. Then import the User class
from user.models import User

# create new app route & specifies methods allowed on new route
## Note: that we have import our routes back into the main app file as well
@app.route('/user/signup', methods=['GET'])
def signup():
    ## another way to write this. the one liner is written below as active code
    ## user = User()
    ## return user.signup()
    
    #creating new class instance
    return User().signup()
    