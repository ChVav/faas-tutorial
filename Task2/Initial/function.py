import json
from urllib import response
import boto3
from PIL import Image
from io import BytesIO


def lambda_handler(event, context):
    """
    Develop a function that saves cropped faces in intermediate bucket that where recognized in pictures of the input bucket
    :param event: contains given input
    :param context:
    :return: categories, number of categories, intermediate path, output path
    """

    # Read the input data


    # Use boto3.client for AWS Rekognition client


    # Use boto3.resource for S3 buckets

    # use the AWS Rekognition client ti detect faces from the opened image


    # loop over the AWS Rekognition response and check the confidence
    for faceDetail in response:

            # Use calculate cropping and use Image.crop to crop the image
            # Follow this link https://blog.devgenius.io/facial-emotion-detection-using-aws-rekognition-in-python-69b2da668192

            # Save the image as PNG and store it on S3

    # Return output data


def calculate_cropping_box(face_detail, image_width, image_height):
    """
    Calculation from https://blog.devgenius.io/facial-emotion-detection-using-aws-rekognition-in-python-69b2da668192
    :param face_detail: face_detail returned from aws recognition
    :param image_width: width of input image
    :param image_height: height of input image
    :return: box with values for cropping the recognized face
    """
    box_width = face_detail['BoundingBox']['Width']
    box_height = face_detail['BoundingBox']['Height']
    box_left = face_detail['BoundingBox']['Left']
    box_top = face_detail['BoundingBox']['Top']

    width = image_width * box_width
    height = image_height * box_height
    left = image_width * box_left
    top = image_height * box_top

    left = int(left)
    top = int(top)
    width = int(width) + left
    height = int(height) + top

    box = (left, top, width, height)

    return box
