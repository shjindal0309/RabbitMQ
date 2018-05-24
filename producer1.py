import pika
import threading

# defualt exchange (exhange='') does round-robin allocation of tasks to consumers

x=0 

def producer(payload,thread_no):

	packet = payload + " " + str(thread_no)

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='hello')
	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body=packet)

	print("Thread %d Sent payload: %s" % (thread_no,payload))
	connection.close()

def main():

	global x

	payload = "hello consumers"
	for thread_no in range(0,4):
		t=threading.Thread(target=producer, args=(payload,thread_no,))
		t.start()

if __name__ == "__main__":
	main()