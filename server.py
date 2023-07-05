from flask import Flask, render_template, request, redirect, session

app =Flask(__name__)

app.secret_key = "This is a Dojo Survey"

	
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    print('request form', request.form)
    print('session', session)
    return redirect('/results')


@app.route('/results')
def result():
    return render_template('results.html', name=session['name'], dojo_location=session['dojo_location'], favorite_language=session['favorite_language'], comments=session['comments'])


@app.route('/')
def home():
    session.clear()
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
    

