from flask import Flask 
from public import public
from admin import admin
from college import college
from university import university
from school import school

from school_board import school_board

from api import api


app=Flask(__name__)

app.secret_key='key'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(college,url_prefix='/college')
app.register_blueprint(university,url_prefix='/university')

app.register_blueprint(school,url_prefix='/school')
app.register_blueprint(school_board,url_prefix='/school_board')
app.register_blueprint(api,url_prefix='/api')
app.run(debug=True,port=5008,host="0.0.0.0")
