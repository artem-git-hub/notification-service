from .module_celery import app
from .utils import send_messages_for_dispatch

@app.task
def send_dispatch_messages(dispatch_id):
    send_messages_for_dispatch(dispatch_id)
