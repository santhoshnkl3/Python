'''
Created on 21-Aug-2018

@author: admin
'''
from flask.app import Flask
from flask.templating import render_template
from flask.globals import request
from flask_mail import Mail,Message

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def sample():
    if request.method=="GET":
        return render_template("bootstrap.html")
    else:
        password=request.form['password']
        emailid=request.form['email']
        semail=request.form['semail']
        pass1=request.form['password']
        message=request.form['message']
        subject1=request.form['subject']


        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = emailid
        app.config['MAIL_PASSWORD'] = password
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        
        mail=Mail(app)
        msg = Message(subject1, sender = emailid, recipients = [semail])
        msg.body = message
        with app.open_resource("logo.png") as fp:
            msg.attach("logo.png", "image/png", fp.read())
        mail.send(msg)
        return "Message sent sucessfully"
    
if __name__ == "__main__":
    app.run(debug=True)    
