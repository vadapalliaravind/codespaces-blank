from confluent_kafka import Consumer, KafkaException, KafkaError
import json

# Configuration for Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  # Start reading at the earliest offset
}

# Initialize the consumer
consumer = Consumer(conf)

# Subscribe to the Kafka topic
consumer.subscribe(['user-events'])

# Function to process messages from Kafka
def consume_event_data():
    try:
        # Poll for new messages (blocking call)
        msg = consumer.poll(timeout=1.0)  # Adjust timeout as needed
        
        if msg is None:
            print("Waiting for new messages...")
            return
        
        if msg.error():
            raise KafkaException(msg.error())
        
        # Deserialize the event data
        event_data = json.loads(msg.value().decode('utf-8'))
        
        # Process the event data (e.g., print or analyze)
        print(f"Received event data: {event_data}")
    
    except Exception as e:
        print(f"Error occurred: {e}")

# Consume messages indefinitely
try:
    while True:
        consume_event_data()
except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    # Close the consumer when done
    consumer.close()
