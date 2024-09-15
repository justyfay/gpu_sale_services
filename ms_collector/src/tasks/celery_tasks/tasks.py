import asyncio

from src.services.construct_data import ConstructData
from src.tasks.celery_tasks.celery_app import celery as app

# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         schedule=10,
#         sig=send_products.s(
#             asyncio.events.get_event_loop().run_until_complete(
#                 ConstructData.construct_product_data())
#         ),
#         queue="product_events",
#     )
#
#
# @app.task()
# def send_products(func):
#     return func


@app.task(name="send_products_from_collector")
def send_products_from_collector():
    return asyncio.events.get_event_loop().run_until_complete(
        ConstructData.construct_product_data()
    )
