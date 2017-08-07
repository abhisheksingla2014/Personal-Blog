from blog import db

class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String())
    content = db.Column(db.String())
    img = db.Column(db.String())
    tag = db.Column(db.Text)
    date = db.Column(db.Text)

    def __repr__(self):
        return "<'{}':{}>".format(self.id,self.tag)


