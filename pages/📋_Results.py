import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import cv2
import numpy as np
import time
import tensorflow as tf

model = tf.keras.models.load_model('waste_vgg16.h5')

def import_n_pred(image_data,model):
    size = (224,224)
    image = cv2.resize(image_data,size)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0) 
    pred = model.predict(image)
    return pred

if 'image' in st.session_state:
    image = st.session_state['image']
    pred = import_n_pred(image,model)
    st.image(image)
    st.subheader(pred)
else:
    st.write("No image is found")
