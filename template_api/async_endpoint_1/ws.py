from flask_restx import Namespace, Resource, abort
from flask_restx.reqparse import RequestParser
from celery.result import AsyncResult

from template_api.async_endpoint_1.tasks import task1
from template_api.celery import celery_app

api = Namespace(
    'async_endpoint_1', description='Example async endpoint'
)


@api.route('/do_job/<string:field1>')
class UpdateAppsResource(Resource):
    reqparse = RequestParser(trim=True)
    reqparse.add_argument(
        'arg1', type=str, location='args'
    )
    reqparse.add_argument(
        'arg2', type=str, location='args'
    )

    @api.expect(reqparse)
    def post(self, field1):
        args = self.reqparse.parse_args()
        arg1 = args.get("arg1")
        arg2 = args.get("arg2")
        
        job = task1.apply_async([field1, arg1, arg2])
        return {'job_id': job.id}


@api.route('/job_status/<string:job_id>')
class CheckJobStatus(Resource):
    
    @api.response(200, "Job finished {'status': 'COMPLETED'}")
    @api.response(206, "Job hasn't finished. {'status': 'PENDING'}")
    @api.response(404, "Parent ID not found. {'status': 'JOB ID NOT FOUND'}")
    def get(self, job_id: str) -> tuple:
        job_result = AsyncResult(job_id, app=celery_app)
        if not job_result:
            abort(404, "Invalid job_id")

        if job_result.ready():
            return job_result.get(), 200

        elif job_result.failed():
            return {'state': 'FAILED'}, 500

        else:
            return {'state': 'PENDING'}, 206


