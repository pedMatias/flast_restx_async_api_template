from template_api.celery import celery_app


@celery_app.task
def task1(arg1: str, arg2: str, arg3: str):
    """
    TODO implement task
    """
    return {"status": "Completed"}
