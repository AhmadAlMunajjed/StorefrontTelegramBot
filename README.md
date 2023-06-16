This is a basic API project built with Flask in Python.

## Prerequisites

You will need Python 3.6+ installed on your machine. 

## Installation

1. Clone the repository to your local machine:

`git clone https://github.com/AhmadAlMunajjed/StorefrontTelegramBot.git`

2. Navigate into the project directory:

`cd StorefrontTelegramBot`

3. Create a virtual environment and activate it:

`python -m venv myenv`
`.\myenv\Scripts\activate`


4. Install the required Python packages:

`pip install -r requirements.txt`


## Running the Application

After installation, you can run the application using Flask's built-in server:

1. Set the FLASK_APP environment variable to your main application file (in this case, `app.py`):

`set FLASK_APP=app.py`


2. Start the server:

`flask run`

## Deployment

This application can be deployed on a cloud platform like AWS Elastic Beanstalk. To deploy this application, you must create a ZIP file containing the necessary files for running the application.

The essential files to include in the ZIP file are:

- `app.py`: This is the main application file where the Flask application is defined.
- `Procfile`: This file is used by certain cloud platforms (like Heroku) to understand how to start your application. This file might not be necessary if you're deploying on AWS Elastic Beanstalk.
- `requirements.txt`: This file contains a list of Python packages required to run the application.

### Steps for Deployment

1. Prepare a ZIP file including the files: `app.py`, `Procfile` (if needed), and `requirements.txt`.
2. Login to your AWS Management Console and go to the AWS Elastic Beanstalk service.
3. Click on "Create a new environment".
4. Select "Web server environment", then click "Select".
5. Fill in the necessary information in the named fields. In the "Platform" section, select "Python" as the platform and leave the platform branch and version as the defaults.
6. In the "Application code" section, select "Upload your code", then click on "Choose file" and select the ZIP file of your application.
7. Click on "Create environment". AWS Elastic Beanstalk will then create the environment and deploy your application.

Please replace the file names with the actual file names in your project if they are different. You might also want to specify the platform version when creating the environment if your application needs a specific Python version.

Also note that you need to ensure the `FLASK_APP` environment variable is set to `app.py` (or whatever your main file is named) in your AWS Elastic Beanstalk environment.

Visit `http://127.0.0.1:5000/` or `http://localhost:5000/` in your web browser to interact with the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.