import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO
import base64

USE_CARD = False

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "6f1ee2649c0b42129fb2775815d9c526"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
ocr_url = vision_base_url + "ocr"

# # Set image_url to the URL of an image that you want to analyze.
# image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
#     "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"

# Set image_path to the local path of an image that you want to analyze.
image_path = "../media/tmp.png"
card1 = "https://raw.githubusercontent.com/yanxi0830/uofthacks/yanxi/iFlushot/media/card1.png?token=ATBbhLRQ_3WsJq3vutE_jhWuVft17E5lks5cTSh7wA%3D%3D"
card2 = "https://raw.githubusercontent.com/yanxi0830/uofthacks/yanxi/iFlushot/media/card2.png?token=ATBbhB1-6IQMnVuDepaZ-kAjEk6Z0Rn-ks5cTSiVwA%3D%3D"
headers    = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'en', 'detectOrientation': 'false'}

def get_card_info(image_path):
    # Captured image to file
    data_url = image_path['url']
    content = data_url.split(';')[1]
    image_encoded = content.split(',')[1]
    body = base64.decodebytes(image_encoded.encode('utf-8'))
    filename = './media/tmp.png'
    with open(filename, 'wb') as f:
        f.write(body)
    
    if USE_CARD:
        data = {'url': card2 }
    else:
        img_data = open(filename, "rb").read()
        data = img_data

    if USE_CARD:
        response = requests.post(ocr_url, headers=headers, params=params, json=data)
    else:
        headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
        response = requests.post(ocr_url, headers=headers, params=params, data=data)
    
    response.raise_for_status()
    analysis = response.json()
    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    # print(line_infos)
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info['text'])
    print(word_infos)

    patient = {}
    patient["first_name"] = word_infos[0] if len(word_infos) > 0 else "John"
    patient["last_name"] = word_infos[1] if len(word_infos) > 1 else "Doe"
    patient["healthcard"] = word_infos[2] if len(word_infos) > 2 else "000000"
    patient["birthdate"] = word_infos[3] if len(word_infos) > 3 else "2000-01-01"
    year = int(word_infos[3][:4]) if len(word_infos) > 3 else 2019
    patient['age'] = 2019 - year
    print(patient)
    return patient