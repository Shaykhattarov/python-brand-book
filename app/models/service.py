from app import db



class Service(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(60), unique=True, nullable=False)
    image: str = db.Column(db.String(20), nullable=True)
    description: str = db.Column(db.String(120), nullable=False)
    essence: str = db.Column(db.String(120), nullable=False)
    development_stages: str = db.Column(db.String(120), nullable=False)
    cost_description: str = db.Column(db.String(120), nullable=False)
    cost: str = db.Column(db.String(20), nullable=False)
    demand: str = db.Column(db.String(120), nullable=False)

    def fetchall(self):
        try:
            services = db.session.query(Service).all()
        except Exception as err:
            print(err)
            return (False, err)
        
        if services is None or len(services) == 0:
            return (False, None)
        else:
            return (True, services)


    def fetch_by_index(self, id):
        try:
            service = db.session.query(Service).get(id)
        except Exception as err:
            print(err)
            return (False, err)
        
        if service is None:
            return (False, None)
        else:
            return (True, service)

    def update_by_index(self, id: int, form):
        try:
            service: Service = db.session.query(Service).get(id)
        except Exception as err:
            print(err)
            return (False, err)
        
        if service is not None:
            service.name = form.name.data
            service.description = form.description.data
            service.essence = form.essence.data
            service.development_stages = form.development_stages.data
            service.cost_description = form.cost_description.data
            service.cost = form.cost.data
            service.demand = form.demand.data

            if form.image.data is not None:
                service.image = form.image.data
            
            db.session.commit()
            return (True, service)
        else:
            return (False, None)


        

    def __repr__(self) -> str:
        return f'<Service - {self.id} - {self.name}>'