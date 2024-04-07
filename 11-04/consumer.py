#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters('178.154.222.166', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume('hello', callback, auto_ack=False)
channel.start_consuming()
