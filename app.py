# import threading
#
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import cv2
# import os
#
# from arduino_service import send_character_to_esp32
#
# app = Flask(__name__)
# CORS(app)
#
#
# # Load the trained model
# model = keras.models.load_model("animal_model.h5")
#
# # Define image size (MUST be defined before use)
# IMG_SIZE = (224, 224)  # Ensure this matches your model's expected input size
#
# # Define categories (Ensure this matches your model's output classes)
# categories = ["Cheetah", "Jaguar", "Leopard", "Lion", "Tiger"]
#
#
# # Function to preprocess uploaded images
# def preprocess_image(image_path):
#     image = cv2.imread(image_path)
#     if image is None:
#         return None
#     image = cv2.resize(image, IMG_SIZE)  # Ensure IMG_SIZE is defined
#     image = image / 255.0
#     image = np.expand_dims(image, axis=0)
#     return image
#
#
# @app.route('/predict', methods=['POST'])
# async def predict_animal():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image file found"}), 400
#
#     file = request.files['image']
#     file_path = "uploaded_image.jpg"
#     file.save(file_path)
#
#     image = preprocess_image(file_path)
#     if image is None:
#         return jsonify({"error": "Invalid image"}), 400
#
#     predictions = model.predict(image)
#     predicted_class = np.argmax(predictions)
#     predicted_animal = categories[predicted_class]
#     animal_to_char = {
#         "Tiger": "A",
#         "Leopard": "B",
#         "Lion": "C",
#         "Cheetah": "D",
#         "Jaguar": "E"
#     }
#     ch = animal_to_char.get(predicted_animal, "Z")
#     threading.Thread(target=send_character_to_esp32, args=(ch,)).start()
#     return jsonify({"animal": categories[predicted_class]})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


import threading

from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import os

from arduino_service import send_character_to_esp32

app = Flask(__name__)
CORS(app)

# Load the trained model
model = keras.models.load_model("animal_model.h5")

# Define image size (MUST be defined before use)
IMG_SIZE = (224, 224)  # Ensure this matches your model's expected input size

# Define categories (Ensure this matches your model's output classes)
categories = ["Cheetah", "Jaguar", "Leopard", "Lion", "Tiger"]


# Function to preprocess uploaded images
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    image = cv2.resize(image, IMG_SIZE)  # Ensure IMG_SIZE is defined
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.route('/predict', methods=['POST'])
async def predict_animal():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found"}), 400

    file = request.files['image']
    file_path = "uploaded_image.jpg"
    file.save(file_path)

    image = preprocess_image(file_path)
    if image is None:
        return jsonify({"error": "Invalid image"}), 400

    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)
    predicted_animal = categories[predicted_class]
    animal_to_char = {
        "Tiger": "A",
        "Leopard": "B",
        "Lion": "C",
        "Cheetah": "D",
        "Jaguar": "E"
    }
    ch = animal_to_char.get(predicted_animal, "Z")
    threading.Thread(target=send_character_to_esp32, args=(ch,)).start()
    return jsonify({"animal": categories[predicted_class]})


if __name__ == '__main__':
    app.run(debug=True)

