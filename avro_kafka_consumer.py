from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError


consumer = AvroConsumer({
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'example.numtest.confluent.testconsumer',
    'schema.registry.url': 'http://localhost:8081',
})
consumer.subscribe(['example.numtest.confluent'])


while True:
    try:
        msg = consumer.poll(10)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue
    elif msg.error():
        print("AvroConsumer error: {}".format(msg.error()))
        continue
    else:
        print(msg.value())

consumer.close()
