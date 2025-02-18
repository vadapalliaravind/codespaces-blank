from confluent_kafka import Producer

# Define a callback function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'client.id': 'python-producer'
}

# Create a producer instance
producer = Producer(conf)

# Send a message to the 'test-topic' topic
topic = 'test-topic'

# Produce a message (you can loop to send multiple messages)
message = 'Hello Kafka!'
producer.produce(topic, message.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered
producer.flush()
