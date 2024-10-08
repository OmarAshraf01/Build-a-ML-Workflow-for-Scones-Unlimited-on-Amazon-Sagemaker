import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2024-09-02-16-24-09-965" ## TODO: fill in

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"]) ## TODO: fill in

    # Instantiate a Predictor
    predictor =sagemaker.predictor.Predictor(endpoint_name=ENDPOINT, sagemaker_session=sagemaker.Session()) ## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image) ## TODO: fill in
    
    # We return the data back to the Step Function    
    event["body"]["inferences"] = json.loads(inferences)
    return {
        'statusCode': 200,
        'body': event["body"]
    }