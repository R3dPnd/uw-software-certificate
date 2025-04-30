In this assignment, you will create a simple Flask web server, deploy it using Docker, and make it accessible through an AWS EC2 instance. This exercise introduces you to key web development concepts, Docker containerization, and cloud deployment.

## Instructions:

1. Set Up Your Flask Application (2 marks)

    * Create your Flask application locally.

    * Your Flask application must have two endpoints:

    * /your_name: This endpoint should return a message like: "Hello world from <your_name>!"

    * /datetime: This endpoint should return the current date and time (remember to install the package)

2. Dockerize Your Application (2 marks)

    * Create a Dockerfile that:

    * Uses Python 3.11-slim as the base image.

    * Copies your Flask app into the container.

    * Installs Flask and any required dependencies.

    * Exposes port 5000.

    * Runs your Flask application upon container startup.

3. GitHub Repository Setup (2 marks)

    * Create a public GitHub repository specifically for this assignment.

    * Push your Dockerfile and Flask application (app.py) to this repository.

    * Clearly document your repository with a brief README.md explaining what the application does and how to run it.

4. DockerHub Deployment (1 mark)

    * Build your Docker container locally and tag it appropriately (e.g., yourdockerhubusername/flask-image:latest).

    * Push your Docker container to DockerHub, ensuring it is publicly accessible.

5. AWS EC2 Instance Deployment (2 marks)

    * Launch a t2.micro AWS EC2 instance.

    * Ensure security group rules allow incoming traffic on port 5000 from anywhere (0.0.0.0/0).

    * Install Docker on your instance.

    * Pull your Docker container from DockerHub and run it on the EC2 instance. ( docker run --rm -d -p 5000:5000 <instance-name> )

Submission Requirements (1 mark)

Provide:

The DockerHub image link (e.g., yourdockerhubusername/flask-image:latest).

The public IP address of your EC2 instance.

A link to your GitHub repository containing the Dockerfile and Flask application.

Marking Rubric (Total 10 Marks):
Flask application correctly implemented with required endpoints: 2 marks

Dockerfile correctly set up and functioning: 2 marks

GitHub repository organized, accessible, and documented clearly: 2 marks

Docker container successfully pushed to DockerHub and accessible: 1 mark

AWS EC2 deployment correctly configured and accessible via public IP: 2 marks

Proper submission of required links and resources: 1 mark

Bonus Enhancement (Extra 1 Bonus Point):
Implement the following enhancement:

Logging Endpoint: Enhance your Flask app by logging each endpoint hit to a file, and create an additional /log endpoint that allows users to view the contents of the log file directly through a browser.

This assignment aims to give you practical experience with Python web frameworks, containerization, and cloud deployment, foundational for any web developer.
