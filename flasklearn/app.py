from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import csv

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(200),nullable=False)
    name=db.Column(db.String(100),nullable=False)
    target=db.Column(db.Integer,nullable=False)

    def __repr__(self) :
        return '<Task %r>' % self.id
@app.route('/details')

def index():
    return render_template('index.html')
        

@app.route('/form',methods=['POST','GET'])

def data():
    if request.method=='GET':
        return 'Hello'
    elif request.method=='POST':
        form_data=request.form

        row=[]
        for key,value in form_data.items():
            if key=='url':
                url=value
            elif key=='name':
                name=value
            elif key=='email':
                email=value
            else:
                target=value

        row=[name,email,target,url]
        print(row)

        with open("storage.csv",'a') as data_file:
            csv_writer=csv.writer(data_file,lineterminator='\n')
            csv_writer.writerow(row)

        return render_template('data.html',form_data=form_data)

        

if __name__=="__main__":
    app.run(debug=True)