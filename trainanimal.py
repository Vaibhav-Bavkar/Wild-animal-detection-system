from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import os

app = Flask(__name__)
CORS(app)

# Define dataset path
DATASET_PATH = os.path.join(os.getcwd(), "dataset")
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20

# Load dataset and preprocess
train_ds = keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True  # Ensure shuffled data
)

# Get class names (ensures correct label order)
class_names = train_ds.class_names
print(f"Class labels assigned: {class_names}")  # Debugging

# Normalize images
normalization_layer = keras.layers.Rescaling(1./255)
train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))

# Enable pre-trained model fine-tuning for better accuracy
base_model = keras.applications.MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
base_model.trainable = True  # Fine-tune for better performance

# Add dropout to reduce overfitting
model = keras.Sequential([
    base_model,
    keras.layers.GlobalAveragePooling2D(),
    keras.layers.Dropout(0.3),  # Dropout to prevent overfitting
    keras.layers.Dense(len(class_names), activation="softmax")
])

# Compile the model
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), 
              loss="sparse_categorical_crossentropy", 
              metrics=["accuracy"])

# Train the model
model.fit(train_ds, epochs=EPOCHS)

# Save model
model.save("animal_model.h5")
print("Model trained and saved as animal_model.h5")
