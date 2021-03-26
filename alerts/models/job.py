from alerts.config import db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Job(db.Model):
    __tablename__ = "job"
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, nullable=False)
    time_execution = db.Column(db.Integer, nullable=False)
    date_execution = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    number_stages = db.Column(db.Integer, nullable=False)
    records_processed = db.Column(db.Integer, nullable=False)
    job_name = db.Column(db.String(120), nullable=False)
    yellow_alert = db.Column(db.Float, nullable=False)
    green_alert = db.Column(db.Float, nullable=False)
    red_alert = db.Column(db.Float, nullable=False)
    
        
    def __init__(self, job_id, time_execution, date_execution, status, number_stages, records_processed, job_name, yellow_alert, green_alert, red_alert):
        self.job_id = job_id
        self.time_execution = time_execution
        self.date_execution = date_execution
        self.status = status
        self.number_stages = number_stages
        self.records_processed = records_processed
        self.job_name = job_name
        self.yellow_alert = yellow_alert
        self.green_alert = green_alert
        self.red_alert = red_alert
        
    def __repr__(self):
        return '' % self.id
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class JobSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Job
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    job_id = fields.Number(required=True)
    time_execution = fields.Number(required=True)
    date_execution = fields.DateTime(required=True)
    status = fields.Number(required=True)
    number_stages = fields.Number(required=True)
    records_processed = fields.Number(required=True)
    job_name = fields.String(required=True)
    yellow_alert = fields.Float(required=True)
    green_alert = fields.Float(required=True)
    red_alert = fields.Float(required=True)
