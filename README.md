# RabbitMQ

**By default RabbitMQ does Round Robin allocation of tasks to consumers**

I have implementation three different models of distributed queues using RabbitMQ. In each implementation consumer is Multiprocessed and producer is Multithreaded

- Multithreaded Producer -> Default Exchange -> Queue_for_each_consumer -> Mutliprocessed Consumers
  * Messages are not persistent and Queue are not durable
  * No acknowledgement used
  * Synchronisation not done at producer level
  * Files are consumer1.py and producer1.py
  
- Producer -> Default Exchange -> Queue_for_each_consumer -> Mutliprocessed Consumers
  * Messages are persistent and Queues are durable
  * Acknowledgement used
  * Load balancing. Not giving more than one task at a time (means After allocating a task to consumer, producer must receive the acknowledgement sent by consumer and only after that the consumer will be allocated next task. If a consumer is busy the task will be allocated to some other consumer)
  * Files are consumer2.py and producer2.py

- Multithreaded Producer -> Self defined Exchange -> Queue_for_each_consumer -> Mutliprocessed Consumers
  * Messages are not persistent and Queue are not durable
  * No acknowledgement used
  * Synchronisation is done at producer level using locks
  * Files are consumer3.py and producer3.py
