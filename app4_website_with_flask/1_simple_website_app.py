#Import Flask object from the flask library
#flask needs to be installed via pip before you can do so
from flask import Flask

#Here we instantiate the Flask object that was imported above
#__name__ is a special variable that gets the name from the python script.
#When Python executes a script Python assigns the name __main__ to the file.
#So when we directly run the script the conditional __name__=="__main__" is True
#which means the script is ran.  However if the script was imported the
#conditional __name__=="__main__" would return to False as the name assigned to
#the script would be __name__=="simple_website_app" and the script would not run.
#This allows for control over the script.
app=Flask(__name__)

#This is a decorator which is directly related to the function below
@app.route('/')

#The function below returns the string and maps it ('/').  In this case your
#webpage is http://127.0.0.1:5000/.  You can change @app.route(/dantest/) and your
#webpage is now on http://127.0.0.1:5000/dantest
def home():
    return "Home Page"

#You can use the decorator and funtions to create multiple pages on your Website
#for example you can have a 'Home Page' and 'Page 1' by using the another decorator
#and function pair.
@app.route('/page1/')
def page1():
    return "Page 1"

if __name__=="__main__":
    app.run(debug=True)
