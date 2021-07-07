# import required packages, libraries and files
import streamlit as st
import detection_file as det_file
from PIL import Image

# page config to change the page icon and the title of the page
st.set_page_config(page_title='Detection In Images', page_icon=':smiley:')

# UI starts from here
st.title('Detection In Images')
st.write('')

# creating a sidebar with various options
operation = ['Home', 'Face Detection', 'Eyes Detection', 'Emotion Detection']
selected = st.sidebar.selectbox(label='Select one of the options...', options=operation, key='key_1')

if selected == 'Home':
    st.write('## Home')
    st.write('This is an app completely dedicated for *study purpose*. In this app, users can upload the image and get the __*face*__, __*eyes*__, __*emotions*__, __*object*__, __*smile*__, etc, detected based on the selected option from the sidebar.')
    st.write("It should be noted that detection is not done on trained data. It is done using the __*Harcascades Files*__. You can visit the harcascades GitHub [here]('https://github.com/opencv/opencv/tree/master/data/haarcascades)")
    st.write('Please select one of the options from the __*left sidebar*__.')
    st.write('')
    st.write("For the code, please visit the GitHub Repository: [Detection_In_Images]('https://github.com/Sandeep-Panchal/Detection_In_Images')")
    st.write('')
    st.write('')

    home_img = Image.open('streamlit_faces.png')
    st.image(home_img)
    st.write('Image Source: [https://cloud.google.com/vision/docs/detecting-faces](https://cloud.google.com/vision/docs/detecting-faces)')

    st.write('')
    st.write('')
    st.write('')
    st.info('As of now, only face and eyes detection is added. Soon I will be adding __*Emotion Detection*__, __*Object Detection*__, __*Detection in Video*__, etc.')

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
    # cascade_file = '../haar-cascade-files-master/haarcascade_frontalface_default'
    # st.warning('Emotion Detection is under maintainence... Please stay tuned for the update on this...')

# displays upload image option only if the page is not Home page
if selected != 'Home':
    uploaded_img = st.file_uploader('Upload an Image', type=['png', 'jpg', 'jpeg'])

# calling the function process_uploaded_image from detection_file
# then based on selected options, we will call face detection or eyes detection or other function
if selected != 'Home' and selected != 'Emotion Detection':
    if uploaded_img is not None:
        img_process = det_file.process_uploaded_image(uploaded_img)

        if selected == 'Face Detection':
            det_file.face_detection(img_process, cascade_file)
        elif selected == 'Eyes Detection':
            det_file.eyes_detection(img_process, cascade_file)

elif selected == 'Emotion Detection':
    st.warning('Emotion Detection will be added soon. Please stay tune for the update on this.')

