import json 
from kafka import KafkaConsumer

TOPIC = 'example.simple_test'
BROKER = 'localhost:29092' # this is the public port exposed by cp-all-in-one 

def json_deserializer(msg):
    return json.loads(msg.decode('utf-8'))

consumer = KafkaConsumer(
    TOPIC,
     bootstrap_servers=[BROKER],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='consumer-group-example',
     value_deserializer=json_deserializer,
     request_timeout_ms=5000.0,
)

for message in consumer:
    print(message.value, message.headers)
