import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO

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
image_path = "/Users/xiyan/Desktop/uofthacks/iFlushot/media/card.png"

image_url = "https://i.pinimg.com/474x/a2/c7/ef/a2c7ef4e3b6d9217fbf102a77027d763.jpg"

# Read the image into a byte array
# image_data = open(image_path, "rb").read()

# headers = {'Ocp-Apim-Subscription-Key': subscription_key}

headers    = {'Ocp-Apim-Subscription-Key': subscription_key}

params  = {'language': 'unk', 'detectOrientation': 'true'}

data    = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
response.raise_for_status()

analysis = response.json()

print(analysis)

# Extract the word bounding boxes and text.
line_infos = [region["lines"] for region in analysis["regions"]]
# print(line_infos)
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
# print(word_infos)



# Display the image and overlay it with the extracted text.
# plt.figure(figsize=(5, 5))
# image = Image.open(BytesIO(requests.get(image_url).content))
# ax = plt.imshow(image, alpha=0.5)
# for word in word_infos:
#     bbox = [int(num) for num in word["boundingBox"].split(",")]
#     text = word["text"]
#     origin = (bbox[0], bbox[1])
#     patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
#     ax.axes.add_patch(patch)
#     plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
# plt.axis("off")