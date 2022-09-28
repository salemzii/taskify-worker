import pika, sys, os, json
import notify


# declare the consumer
def Consumer():

    params = pika.URLParameters("amqps://yxqtjffp:x5EMaWMA_MtzVqh3Xmrl7MqU7-6RVVuO@whale.rmq.cloudamqp.com/yxqtjffp") #replace with env placeholder
    
    conn = pika.BlockingConnection(parameters=params)
    channel = conn.channel()
    channel.queue_declare("taskifyQ")

    def callback(ch, method, properties, body):
        print("[x] Received %r" % body)
        notify.CreateNotification(notification=json.loads(body))
        return

    channel.basic_consume(queue='taskifyQ', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    return


if __name__ == '__main__':
    try:
        Consumer()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)