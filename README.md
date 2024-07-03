# DTQ-Celery
This project demonstrates how to set up a distributed task queue using Celery with RabbitMQ or Redis as the message broker. The system allows you to distribute and manage tasks asynchronously across multiple worker nodes. Additionally, it includes a monitoring tool, Flower, for real-time task monitoring and management.
## Features
Asynchronous Task Processing: Distribute tasks to worker nodes for parallel execution.
Support for RabbitMQ and Redis: Choose either RabbitMQ or Redis as the message broker.
Task Retry Mechanism: Automatically retry failed tasks with customizable retry logic.
Real-time Monitoring: Monitor and manage tasks using the Flower web interface.
## Prerequisites
Python (3.6 or later)
Virtual environment (optional but recommended)
RabbitMQ or Redis installed and running