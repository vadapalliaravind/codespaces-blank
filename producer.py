from confluent_kafka import Producer
import json

# Configuration for Kafka producer

conf = {
    'bootstrap.servers': 'localhost:9092',  # Use localhost or the Docker IP
    'client.id': 'python-producer',
    'acks': 'all',
    'retries': 3,
    'linger.ms': 1,
    'batch.num.messages': 1000
}


# Initialize the producer
producer = Producer(conf)

# Function to send message to Kafka
def send_event_data(topic, event_data):
    # Convert event data to JSON (or any other format as required)
    message = json.dumps(event_data)
    
    # Produce the message to Kafka topic
    producer.produce(topic, value=message)
    producer.flush()

# Sample event data (e.g., user interaction)
event_data = {
    "user_id": "user_123",
    "action": "click",
    "timestamp": "2025-02-15T14:30:00",
    "page": "homepage"
}

# Send the event data to Kafka topic "user-events"
send_event_data('user-events', event_data)

print(f"Sent event data: {event_data}")
