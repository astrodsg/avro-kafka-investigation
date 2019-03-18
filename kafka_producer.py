"""
CREATE STREAM EXAMPLE_SIMPLE_TEST \
  (
    number BIGINT \
  ) \
  WITH (
    KAFKA_TOPIC='example.simple_test', \
    VALUE_FORMAT='JSON' \
  );
"""
import json 
from kafka import KafkaProducer

TOPIC = 'example.simple_test'
BROKER = 'localhost:29092' # this is the public port exposed by cp-all-in-one 

def json_serializer(msg):
    return json.dumps(msg).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=[BROKER], # send to the broker
    client_id="example-kafka-producer",
    acks=1, # acknowledge against local queue
    value_serializer=json_serializer,
)

headers = [
    ('schema', json_serializer('v0')),
]
for i in range(10):
    data = {'number': i}
    producer.send(TOPIC, value=data, headers=headers)
