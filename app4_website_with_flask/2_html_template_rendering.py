#In order to display html pages from our Python app we need to import The
#render_template from our flask library.  This will allow our functions to
#return html pages instead of just strings.
from flask import Flask, render_template

app=Flask(__name__)

#In the functions below we return html pages instead of strings.  In order for
#this to work the html pages need to placed in a folder called "templates" in
#the same directory as the python script

@app.route('/')
def home():
#    return "Home Page"
    return render_template("home.html")

@app.route('/page1/')
def page1():
#    return "Page 1"
    return render_template("page1.html")

if __name__=="__main__":
    app.run(debug=True)
