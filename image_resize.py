import boto3
from io import BytesIO
from PIL import Image


def resize_image(image_bytes, width, height):
    """Resize an image to the specified dimensions.

    Args:
        image_bytes (bytes): Image bytes to resize.
        width (int): Width of the output image.
        height (int): Height of the output image.

    Returns:
        bytes: Resized image bytes.
    """
    with Image.open(BytesIO(image_bytes)) as img:
        img.thumbnail((width, height))
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        return buffer.getvalue()


def lambda_handler(event, context):
    """AWS Lambda function to resize images.

    Args:
        event (dict): AWS Lambda event object.
        context (object): AWS Lambda context object.

    Returns:
        dict: Resized image data.
    """
    # Retrieve input data from the event object
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']
    width = event.get('width', 300)
    height = event.get('height', 300)

    # Download the image from S3
    s3_client = boto3.client('s3')
    image_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    image_bytes = image_object['Body'].read()

    # Resize the image
    resized_image = resize_image(image_bytes, width, height)

    # Upload the resized image to S3
    output_key = f"resized_{width}x{height}_{s3_key}"
    s3_client.put_object(Bucket=s3_bucket, Key=output_key, Body=resized_image)

    # Return the resized image information
    return {
        'bucket': s3_bucket,
        'key': output_key,
        'width': width,
        'height': height,
    }
