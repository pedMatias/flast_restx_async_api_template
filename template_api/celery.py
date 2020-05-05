from celery import Celery

from template_api import settings


celery_app = Celery(
    'tasks',
    backend='redis://{}:{}/0'.format(
        settings.REDIS['host'],
        settings.REDIS['port']
    ),
    broker='redis://{}:{}/0'.format(
        settings.REDIS['host'],
        settings.REDIS['port']
    )
)


# Register tasks from sub-modules
celery_app.autodiscover_tasks(['template_api.async_endpoint_1.tasks'])

