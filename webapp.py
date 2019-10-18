from flask import Flask, url_for, render_template, request

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
    USD = request.args['USD']
    response = float(USD) * 7.08
    
    return render_template('response.html', responseFromServer=response)
    
@app.route("/response2")
def render_response2():
    Miles = request.args['Miles']
    response = float(Miles) * 1.609
    
    return render_template('response2.html', responseFromServer=response)
    
@app.route("/response3")
def render_response3():
    Peso = request.args['Peso']
    response = float(Peso) * 0.052
    
    return render_template('response3.html', responseFromServer=response)
if __name__=="__main__":
    app.run(debug=False)
