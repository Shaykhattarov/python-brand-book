from app import db


class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"<Discussion {self.id} - {self.name}>"