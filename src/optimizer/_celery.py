from celery import Celery

from config import Setting


settings = Setting()
host = settings.REDIS_HOST.get_secret_value()
port = settings.REDIS_PORT.get_secret_value()
db = settings.REDIS_DB.get_secret_value()

# Celery application
celery = Celery(
    "tourist_ai",
    broker=f"redis://{host}:{port}/{db}",
    backend=f"redis://{host}:{port}/{db}",
    include=["optimizer.main"]
)

# Configure
celery.conf.update(
    timezone='Asia/Tokyo',
    enable_utc=True,
    
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    
    result_expires=3600, # 1 hour
    
    worker_prefetch_multiplier=1,
    task_acks_late=True,
)
