from src.tasks.celery_app import celery


@celery.task(name="send_products_from_collector")
def send_products(products):
    return products
