from confluent_kafka import Consumer, KafkaException, KafkaError

# Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': 'python-consumer-group',    # Consumer group ID
    'auto.offset.reset': 'earliest'         # Start reading from the earliest message
}

# Create a consumer instance
consumer = Consumer(conf)

# Subscribe to the topic 'test-topic'
consumer.subscribe(['test-topic'])

# Consume messages (you can loop to consume indefinitely)
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Poll for messages with a 1-second timeout
        if msg is None:
            continue  # No message available
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"End of partition reached {msg.partition()}, offset {msg.offset()}")
            else:
                raise KafkaException(msg.error())
        else:
            print(f"Consumed message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass
finally:
    # Close the consumer when done
    consumer.close()
