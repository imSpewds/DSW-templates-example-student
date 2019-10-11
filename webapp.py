from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1") #annotations tell which function goes with which request
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route("/response")
def render_response():
    favorite_color = request.args['color'] #get user's input for color input
    if favorite_color == "red":
        response = "Thats my favorite color too!"
    else:
        response = "My favorite color is red."
    return render_template('response.html', responseFromServer=response)
    
if __name__=="__main__":
    app.run(debug=False)
