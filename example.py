''' Student Repository Website '''

from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! This is Flask"

@app.route('/Goodbye')
def see_ya():
    return "See ya later!"

@app.route('/sample_template')
def template_demo():
    return render_template('parameters.html',
                            title='Stevens Repository',
                            my_header='my Stevens Repository',
                            my_param='my custom parameter')

app.run(debug=True)
