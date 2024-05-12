import pika
import json
from mongoengine import connect, Document, StringField, BooleanField
from bson import ObjectId

connect('contacts_db')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)

def send_email(contact_id):
    contact = Contact.objects.get(id=ObjectId(contact_id))
    contact.message_sent = True
    contact.save()
    print(f"Повідомлення надіслано контакту з ID {contact_id}")

def callback(ch, method, properties, body):
    contact_data = json.loads(body)
    contact_id = contact_data['contact_id']
    send_email(contact_id)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='contacts')

channel.basic_consume(queue='contacts', on_message_callback=callback, auto_ack=True)

print('Очікування повідомлень з черги RabbitMQ...')

channel.start_consuming()