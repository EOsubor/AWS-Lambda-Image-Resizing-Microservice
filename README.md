# AWS-Lambda-Image-Resizing-Microservice

This microservice is built using AWS Lambda and provides a simple REST API for resizing images. It can be used in various applications where image resizing is required, such as eCommerce sites or image galleries.


### Setup
- Clone this repository to your local machine
- Install the required dependencies using npm install
- Create an S3 bucket to store the images
- Update the configuration in serverless.yml file to specify the S3 bucket name and region
- Deploy the microservice using serverless deploy command
- The endpoint URL will be displayed in the console upon successful deployment


### Usage

To resize an image, make a POST request to the API endpoint with the following parameters:

- `key`: The S3 object key of the original image
- `width`: The desired width of the resized image
- `height`: The desired height of the resized image

Example request:

```
curl -X POST https://example.com/resize \
  -H 'Content-Type: application/json' \
  -d '{ "key": "example.jpg", "width": 400, "height": 300 }'
```

Example response:

```
{
  "success": true,
  "url": "https://example-bucket.s3.amazonaws.com/example_400x300.jpg"
}
```


### Architecture

This microservice is built using the following technologies:

- AWS Lambda: Serverless computing platform for running the image resizing function
- Serverless Framework: Framework for building and deploying serverless applications
- Node.js: JavaScript runtime for executing the image resizing function
- Sharp: Node.js module for image resizing and manipulation
- Amazon S3: Object storage service for storing the original and resized images


### License

This microservice is licensed under the MIT License. See the LICENSE file for details.
