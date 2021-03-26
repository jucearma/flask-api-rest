from alerts.models.job import Job,JobSchema
from alerts.config import db

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)
db.create_all()

class Job_Services:
    
    def add_job(self, job:Job):
        db.session.add(job)
        db.session.commit()


    def find_all_jobs(self):
        get_jobs = Job.query.all()
        return jobs_schema.dump(get_jobs)

    
    def get_job_by_id(self,id: int):
        get_job = Job.query.get_or_404(id)
        return job_schema.dump(get_job)

    
    def update_job_by_id(self, id:int, data):
        get_job = Job.query.get_or_404(id)
        if data.get('job_id'):
            get_job.job_id = data['job_id']
        if data.get('time_execution'):
            get_job.time_execution = data['time_execution']
        if data.get('date_execution'):
            get_job.date_execution = data['date_execution']
        if data.get('status'):
            get_job.status= data['status']
        if data.get('number_stages'):
            get_job.number_stages= data['number_stages']
        if data.get('records_processed'):
            get_job.records_processed= data['records_processed']
        if data.get('job_name'):
            get_job.job_name= data['job_name']
        if data.get('yellow_alert'):
            get_job.yellow_alert= data['yellow_alert']
        if data.get('green_alert'):
            get_job.green_alert= data['green_alert']
        if data.get('red_alert'):
            get_job.red_alert= data['red_alert']
        self.add_job(get_job)
        job_schema = JobSchema(only=['job_id', 'time_execution', 'date_execution','status','number_stages', 'records_processed', 'job_name', 'yellow_alert', 'green_alert', 'red_alert'])
        
        return job_schema.dump(get_job)

    
    def create_job(self,data):
        job = job_schema.load(data)
        return job_schema.dump(job.create())
    
    
    def delete_job_by_id(self, id):
        get_job = Job.query.get_or_404(id)
        db.session.delete(get_job)
        db.session.commit()
        return str("Job {} removed successfully".format(id))