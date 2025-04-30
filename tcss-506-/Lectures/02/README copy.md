# TCSS 506 Assignment 02: Hello World Flask API

This repository contains the implementation of a simple "Hello World" API built using Flask, a lightweight Python web framework. The project is part of the TCSS 506 coursework and serves as an introduction to building RESTful APIs.

## Features

- A basic Flask application setup.
- A single API endpoint that returns a "Hello, World!" message.
- Demonstrates the use of Flask for creating web APIs.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/tcss-506-assignment-02-hello-world-flask-api.git
    cd tcss-506-assignment-02-hello-world-flask-api
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Access the API in your browser or via a tool like `curl` or Postman:
    ```
    http://127.0.0.1:5000/
    ```

    The API will respond with:
    ```json
    {
         "message": "Hello, World!"
    }
    ```

## Project Structure

```
tcss-506-assignment-02-hello-world-flask-api/
│
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
