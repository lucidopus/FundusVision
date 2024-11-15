# Cataract Detection Project

This project implements a deep learning model using **VGG19** to classify fundus images as either "Normal" or "Cataract". Additionally, it provides a **Flask** web application where users can upload fundus images and receive predictions on the likelihood of cataracts. The model is trained on a dataset of labeled fundus images, preprocessed and prepared in Google Colab.

## Overview

The project consists of two main parts:

1. **Model Training**: A CNN model built on VGG19, trained and validated on preprocessed fundus images to detect cataracts.
2. **Web Application**: A simple Flask app that allows users to upload images and see if cataracts are detected. The app is hosted locally and uses the trained model to make predictions.

## Dataset

The dataset consists of fundus images labeled with diagnostic keywords such as "normal" or "cataract". Images are categorized into:
- **Cataract images**: Fundus images diagnosed with cataract.
- **Normal images**: Fundus images without cataract.

The images are preprocessed to a size of **224x224 pixels** to match the input requirements of VGG19.

## Model Architecture

The project leverages the **VGG19** architecture with pre-trained weights on ImageNet:
1. **Feature Extraction**: Using the convolutional layers of VGG19 (frozen during training).
2. **Fully Connected Layers**: Flattened features are passed to a dense layer with sigmoid activation to predict probabilities for binary classification.
3. **Compilation and Training**: The model uses **binary cross-entropy** loss and **Adam** optimizer, with callbacks for early stopping and checkpointing.

### Model Layers Summary
```plaintext
- VGG19 pre-trained layers (Frozen)
- Flatten Layer
- Dense Layer (1 neuron, sigmoid activation)
```

## Flask Web Application

The web application allows users to interact with the trained model through a user-friendly interface. It provides functionalities to upload images, view predictions, and manage uploaded files.

### Features

1. **Image Upload**: Users can upload fundus images in various formats (JPEG, PNG).
2. **Prediction Display**: After uploading, users receive real-time predictions from the model indicating whether the image shows a "Normal Fundus" or "Cataract Detected!".
3. **File Management**: The application includes a refresh functionality to remove uploaded images from the server after use, ensuring a clean state for future uploads.

### Key Endpoints

- **`/`**: This is the main route where users can upload images. If the upload is successful, the user is redirected to the same page to view the uploaded image.
- **`/getPrediction`**: This route processes the uploaded image, performs the prediction using the trained model, and returns the result as a string.
- **`/display/<filename>`**: This endpoint displays the uploaded image for the user.
- **`/refresh`**: This route allows users to delete the uploaded image from the server, facilitating a fresh start for new uploads.

### Application Workflow

1. **Upload an Image**:
   - Users visit the home page and upload an image file using the provided form. If the file is valid, it is saved to the `static/uploads` directory.

2. **Get Prediction**:
   - Once an image is uploaded, the user can click to retrieve predictions. The uploaded image is read, resized, and fed into the model for classification. The result is displayed on the webpage.

**Demo** : https://drive.google.com/file/d/1Fa3c8A-tvAJblfip-2vZMkzbxDllQVCA/view?usp=share_link
