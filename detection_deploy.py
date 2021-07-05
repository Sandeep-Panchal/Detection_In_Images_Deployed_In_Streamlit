import streamlit as st
import pandas as pd
import cv2
from PIL import Image
import numpy as np

st.write('# Detection...')

# creating a sidebar with various options
operation = ['Home', 'Face Detection', 'Eyes Detection', 'Emotion Detection']
selected = st.sidebar.selectbox(label='Choose one of the following...', options=operation)

if selected == 'Home':
    st.write('## Home')
    st.write('This is a app wherein users can upload the image and get the face, eyes, emotion detected based on the selected option from the sidebar.')
    st.write('Please select one of the options from the left sidebar.')

elif selected == 'Face Detection':
    st.write('## {}'.format(selected))
    st.write('Please upload an image. It will detect eyes and draw box around the detected face.')
    cascade_file = 'haar-cascade-files/haarcascade_frontalface_default.xml'

elif selected == 'Eyes Detection':
    st.write('## {}'.format(selected))
    st.write('Please upload an image. It will detect eyes and draw boxes around the detected eyes.')
    cascade_file = 'haar-cascade-files/haarcascade_eye.xml'

# elif selected == 'Emotion Detection':
    # st.write('## {}'.format(selected))
    # st.write('Please upload an image. It will detect emotion of a human.')
    # cascade_file = 'haar-cascade-files/haarcascade_frontalface_default'
    # st.warning('Emotion Detection is under maintainence... Please stay tuned for the update on this...')

# displays upload image option only if the page is not Home page
if selected != 'Home':
    uploaded_img = st.file_uploader('Upload an Image', type=['png', 'jpg', 'jpeg'])

# processing the uploaded image such as detecting eyes, face, emotions as per the user's selected option
def process_uploaded_image(uploaded_img, cascade_file):
    
    img_open = Image.open(uploaded_img)
    img_array = np.array(img_open)
    img_cvt = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    cascade_class = cv2.CascadeClassifier(cascade_file)
    found_part = cascade_class.detectMultiScale(img_cvt, 1.3, 5)

    if found_part is ():
        st.error('Detection Failed...')
    else:
        xl, yl, wl, hl = [], [], [], []
        for f in found_part:
            x, y, w, h = f
            cv2.rectangle(img_cvt, (x,y), (x+w, y+h), (0,255,0), 3)
            xl.append(x)
            yl.append(y)
            wl.append(w)
            hl.append(h)
        
        st.write()
        st.write()
        st.image(img_cvt, channels='BGR', width=500)
        st.write()
        st.write('### Face Detected and Co-Ordinates are:')
        st.write(pd.DataFrame({'X':xl, 'Y':yl, 'W':wl, 'H':hl}))

if selected != 'Home' and selected != 'Emotion Detection':
    if uploaded_img is not None:
        process_uploaded_image(uploaded_img, cascade_file)
elif selected == 'Emotion Detection':
    st.warning('Emotion Detection is under maintainence... Please stay tuned for the update on this...')
