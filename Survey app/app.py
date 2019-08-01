from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://besssdukztauju:1e2197d78192bbedfbc1721933d504025815ff4b722d55f09f7a9629b1177210@ec2-54-83-1-101.compute-1.amazonaws.com:5432/d9f891gl9orj1p?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(80),unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email_,height):
        self.email_=email_
        self.height=height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if(db.session.query(Data).filter(Data.email_==email).count()==0):
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height)).scalar()
            max_height=db.session.query(func.max(Data.height)).scalar()
            min_height=db.session.query(func.min(Data.height)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height).count()
            send_email(email,height,average_height,count,max_height,min_height)
            return render_template("success.html")
        return render_template("index.html",text="Seems like we've got something from that email address already!")

if __name__ == '__main__':
    app.debug=True
    app.run()
