
import gradio as gr
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load your model (make sure the model file is accessible)
model = load_model('DN_.h5')

# Function to preprocess the uploaded image and make predictions
def predict_image(img):
    img.save("temp_image.jpg")
    preprocessed_image = prepare_image("temp_image.jpg")
    preprocessed_image = preprocessed_image.reshape(1, 128, 128, 3)
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions)
    return "Prediction: Real Image" if predicted_class == 0 else "Prediction: Tampered Image"

# Gradio Interface
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Tampering Detection",
    description="Upload an image to check for tampering using the DenseNet model."
)

# Launch the Gradio interface
interface.launch(share=True)
