# Image Resizing Microservice using AWS Lambda

This microservice allows you to resize images using AWS Lambda. The microservice takes an image as input and returns a resized image in the desired dimensions. The microservice is deployed using the AWS SAM (Serverless Application Model).

### Prerequisites

Before deploying this microservice, ensure that you have the following installed:

- AWS CLI
- AWS SAM CLI
- Python 3.8 or higher
- Pillow library (to be installed in the virtual environment)

### Installation

- Clone this repository.
- Create a virtual environment by running `python3 -m venv env`.
- Activate the virtual environment by running `source env/bin/activate`.
- Install the required packages by running `pip install -r requirements.txt`.
- Navigate to the root of the repository and run sam build to build the AWS SAM package.
- Run `sam deploy --guided` to deploy the application. Follow the prompts to configure the deployment.


### Usage

To resize an image, send a POST request to the endpoint provided by AWS API Gateway, with the following parameters:

`width`: The desired width of the resized image.
`height`: The desired height of the resized image.
`image`: The image file to be resized.

The microservice will return the resized image in the response.


Example:

```
import requests

url = 'https://your_api_gateway_endpoint'
params = {
    'width': 500,
    'height': 500,
}
files = {
    'image': open('path/to/image.jpg', 'rb')
}

response = requests.post(url, data=params, files=files)
resized_image = response.content
```


### Improvements

- Added support for multiple image file types (JPEG, PNG, BMP, GIF, and TIFF).
- Added error handling for invalid image dimensions and unsupported image file types.
- Optimized image quality and reduced file size.


### Architecture

This microservice is built using the following technologies:

- Python 3.7+
- AWS API Gateway
- Pillow: Python Imaging library
- AWS Lambda: Serverless computing platform for running the image resizing function
- Serverless Framework: Framework for building and deploying serverless applications
- Boto3: AWS SDK for Python
- Amazon S3: Object storage service for storing the original and resized images


### License

This microservice is licensed under the MIT License. See the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
