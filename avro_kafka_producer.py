from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


value_schema = avro.load('schemas/schema_v0.json')

producer = AvroProducer({
      'bootstrap.servers': 'localhost:29092',
      'schema.registry.url': 'http://localhost:8081',
    },
    default_value_schema=value_schema,
)

for i in range(20):
    data = {"name": "Alyssa", "age": i}
    producer.produce(
        topic='example.numtest.confluent',
        value=data,
    )

# must include flush to send messages
producer.flush()
