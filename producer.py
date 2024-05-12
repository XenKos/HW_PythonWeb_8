import pika
import json
from mongoengine import connect, Document, StringField, BooleanField
from bson import ObjectId
from faker import Faker

connect('contacts_db')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)

def create_fake_contacts(num_contacts):
    fake = Faker()
    contacts = []
    for _ in range(num_contacts):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email()
        )
        contact.save()
        contacts.append(contact)
    return contacts

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='contacts')

fake_contacts = create_fake_contacts(5)
for contact in fake_contacts:
    contact_data = {
        'contact_id': str(contact.id)
    }
    channel.basic_publish(exchange='', routing_key='contacts', body=json.dumps(contact_data))

print("Фейкові контакти створені та надіслані в чергу RabbitMQ")

connection.close()