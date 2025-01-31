import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def run_model(model_path, input_image_path, img_width= 150, img_height=150):
    # Load the trained model
    model = load_model(model_path)
    img = load_img(input_image_path, target_size=(img_width, img_height))
    img_array = img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])

    class_labels = ['acne', 'hyperpigmentation', 'Nail_psoriasis', 'SJS-TEN', 'Vitiligo']

    return f'{class_labels[predicted_class_index]}'

