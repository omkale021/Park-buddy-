import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2

# Define the CNN model
def create_cnn_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(36, activation='softmax')  # Assuming 36 characters (A-Z and 0-9)
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

model = create_cnn_model()

# Train the model (you need a dataset for this)
def train_model(model, train_data_dir, validation_data_dir):
    train_datagen = ImageDataGenerator(rescale=1./255)
    validation_datagen = ImageDataGenerator(rescale=1./255)
    
    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical'
    )
    
    validation_generator = validation_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical'
    )
    
    model.fit(
        train_generator,
        steps_per_epoch=2000,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=800
    )

# Assuming you have the directories set up with your dataset
# train_model(model, 'data/train', 'data/validation')

# For prediction
def predict_license_plate(model, image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (64, 64))
    image = np.expand_dims(image, axis=0) / 255.0
    prediction = model.predict(image)
    return np.argmax(prediction, axis=1)

# Assuming 'license_plate.jpg' is the image you want to predict
predicted_license_plate = predict_license_plate(model, 'license_plate.jpg')
print(predicted_license_plate)
