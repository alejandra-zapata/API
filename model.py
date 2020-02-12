from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Program(db.Model):
    """ Program """

    __tablename__= "program"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(1000)) 

class Section(db.Model):
    """ Section """

    __tablename__= "section"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"))
    name = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    order_index = db.Column(db.Integer) 
    image_link = db.Column(db.String(200))
    is_last = db.Column(db.Boolean)

    program = db.relationship("Program", backref=db.backref("section"))
    

class Activity(db.Model):
    """ Activity """

    __tablename__= "activity"

    id = db.Column(db.Integer, autoincrement=True,  primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey("section.id"))
    html_content = db.Column(db.String(1000))
    question = db.Column(db.String(500))

    section = db.relationship("Section", backref=db.backref("activity"))

class Answer(db.Model):
    """ Answer """

    __tablename__= "answer"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"))
    answer_text = db.Column(db.String(500))

    activity = db.relationship("Activity", backref=db.backref("answer"))


##################
# Helper functions

def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")