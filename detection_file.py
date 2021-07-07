# import required packages, libraries and files
import cv2
from PIL import Image
import pandas as pd
import numpy as np
import streamlit as st

# processing the uploaded image
def process_uploaded_image(uploaded_img):
    
    img_open = Image.open(uploaded_img)
    img_array = np.array(img_open)
    img_cvt = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    return img_cvt

# function to detect face
def face_detection(img_process, face_file):
    
    cascade_face = cv2.CascadeClassifier(face_file)
    found_face = cascade_face.detectMultiScale(img_process, 1.3, 5)

    if found_face is ():
        st.error('Detection Failed...')
    else:
        xl, yl, wl, hl = [], [], [], []
        for f in found_face:
            x, y, w, h = f
            cv2.rectangle(img_process, (x,y), (x+w, y+h), (0,255,0), 3)
            xl.append(x)
            yl.append(y)
            wl.append(w)
            hl.append(h)
        
        st.write()
        st.write()
        st.image(img_process, channels='BGR', width=500)
        st.write()
        st.write('### Detected Co-Ordinates are:')
        st.write(pd.DataFrame({'X':xl, 'Y':yl, 'W':wl, 'H':hl}))

    # return found_face

# function to detect eyes
# below function will be called only if the face is detected
def eyes_detection(img_process, eyes_file):

    # found_face = face_detection(img_process, cascade_face)
    cascade_eyes = cv2.CascadeClassifier(eyes_file)
    found_eyes = cascade_eyes.detectMultiScale(img_process, 1.3, 5)

    if found_eyes is ():
        st.error('Detection Failed...')
    else:
        xl, yl, wl, hl = [], [], [], []
        for f in found_eyes:
            x, y, w, h = f
            cv2.rectangle(img_process, (x,y), (x+w, y+h), (0,255,0), 3)
            xl.append(x)
            yl.append(y)
            wl.append(w)
            hl.append(h)
        
        st.write()
        st.write()
        st.image(img_process, channels='BGR', width=500)
        st.write()
        st.write('### Detected and Co-Ordinates are:')
        st.write(pd.DataFrame({'X':xl, 'Y':yl, 'W':wl, 'H':hl}))