from faststream import FastStream
from faststream.rabbit import ExchangeType, RabbitBroker, RabbitExchange, RabbitQueue
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_faststream import BrokerWrapper, StreamScheduler

from config import settings
from src.services.construct_data import ConstructData

broker = RabbitBroker(settings.broker_url)
taskiq_broker = BrokerWrapper(broker)

app = FastStream(broker)


@app.after_startup
async def declare_smth():
    await broker.declare_exchange(
        RabbitExchange(
            name="product_events",
            type=ExchangeType.DIRECT,
        )
    )

    await broker.declare_queue(
        RabbitQueue(
            name="product_events",
            durable=True,
        )
    )


taskiq_broker.task(
    message=ConstructData.construct_product_data,
    queue="product_events",
    schedule=[{"cron": "* * * * *"}],
)

scheduler = StreamScheduler(
    broker=taskiq_broker, sources=[LabelScheduleSource(taskiq_broker)]
)
