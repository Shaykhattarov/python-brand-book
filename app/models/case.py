from app import db


class Case(db.Model):
    __tablename__ = "case"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(60), nullable=False)
    positioning = db.Column(db.String(120), nullable=False)
    mission = db.Column(db.String(120), nullable=False)
    emotions = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return '<Case - {} - {}>'.format(self.id, self.name)
    
    def fetchall(self):
        try:
            cases = db.session.query(Case).all()
        except Exception as err:
            print(err)
            return (False, err)
        
        if cases is None or len(cases) == 0:
            return (False, None)
        else:
            return (True, cases)

    def fetch_by_index(self, id: int):
        try:
            cases = db.session.query(Case).get(id)
        except Exception as err:
            print(err)
            return (False, err)
        
        if cases is None:
            return (False, None)
        else:
            return (True, cases)