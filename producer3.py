import pika
import threading
import time

seq_no =0 

def producer(lock,payload,thread_no):

	global seq_no

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.exchange_declare(exchange='logs',
	                         exchange_type='fanout')

	while(1):
		
		lock.acquire()
		packet=str(payload)+","+str(thread_no)+","+str(seq_no)
		channel.basic_publish(exchange='logs',
		                      routing_key='',
		                      body=packet)

		print("Thread %d Sent packet having Payload : %d & Seq_no : %d" % (thread_no,payload,seq_no))
		seq_no+=1
		payload = 2*seq_no
		lock.release()

		time.sleep(1)
		
	connection.close()

def main():

	global seq_no

	lock = threading.Lock()

	threads = []
	payload = 2*seq_no
	for thread_no in range(0,4):
		threads.append(threading.Thread(target=producer, args=(lock,payload,thread_no,)))
	
	for thread_no in range(0,4):
		threads[thread_no].start()

if __name__ == "__main__":
	main()