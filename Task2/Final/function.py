import json
import boto3
from PIL import Image
from io import BytesIO


def lambda_handler(event, context):
    """
    saves cropped faces in intermediate bucket that where recognized in pictures of input bucket
    :param event: contains given input
    :param context:
    :return: categories, number of categories, intermediate path, output path
    """
    picture_path = event['filePaths']
    input_bucket_name = event['arnInputBucket']
    intermediate_bucket_name = event['arnIntermediateBucket']
    output_bucket_name = event['arnOutputBucket']

    recognition_client = boto3.client('rekognition')

    s3 = boto3.resource('s3')
    input_bucket = s3.Bucket(input_bucket_name)
    intermediate_bucket = s3.Bucket(intermediate_bucket_name)

    picture_object = input_bucket.Object(picture_path)
    object_response = picture_object.get()
    picture_file_stream = object_response['Body']
    image = Image.open(picture_file_stream)

    image_width, image_height = image.size
    counter = 0
    emotion_set = set()

    response = recognition_client.detect_faces(Image={'S3Object': {'Bucket': input_bucket_name, 'Name': picture_path}},
                                               Attributes=['ALL'])
    for faceDetail in response['FaceDetails']:
        confidence = faceDetail['Confidence']
        if float(confidence) >= 97.0:  # only continue if confidence of face recognition more than 97%
            counter = counter + 1
            emotion = faceDetail['Emotions'][0]['Type']
            emotion_set.add(emotion)

            box = calculate_cropping_box(faceDetail, image_width, image_height)
            cropped_image = image.crop(box)

            buffer = BytesIO()
            cropped_image.save(buffer, "PNG")
            buffer.seek(0)
            intermediate_bucket.put_object(Key=emotion + "/cropped_" + str(counter) + "_" + picture_path + ".png", Body=buffer)

    emotion_list = list(emotion_set)
    return {
        "categories": emotion_list,
        "numCategories": len(emotion_list),
        "arnIntermediateBucket": intermediate_bucket_name,
        "arnOutputBucket": output_bucket_name
    }


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
