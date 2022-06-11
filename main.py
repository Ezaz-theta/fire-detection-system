from cv2 import COLOR_BGR2RGB
import streamlit as st
import pandas as pd
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os
import device
import time ,sys
import cv2
import numpy as np
import time
import sys
import fire_net as fn

def object_detection_image():
    st.title('Object Detection for Images')
    st.write("""
    This feature takes in an image and outputs the image with bounding boxes created around the objects in the image
    """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])
    if file!= None:
        file.name="test."+str(file.type[6:])
        img1 = Image.open(file)
        with open("./"+file.name,"wb") as f:
            f.write(file.getbuffer())
        img2 = np.array(img1)
        det_img,detections = fn.detect_from_image(file.name,"file")
        st.write("Uploaded Image:")
        st.image(img1)
        st.write("Detections:")
        if(len(detections) != 0):
            st.image(cv2.cvtColor(det_img,cv2.COLOR_BGR2RGB))
        else:
            st.write("No Fire Detected")
        os.remove(file.name)

def object_detection_video():
    #object_detection_video.has_beenCalled = True
    st.title("Object Detection for Videos")
    st.write("""
    This feature takes in a video and outputs the video with bounding boxes created around the objects in the video 
    """
    )
    uploaded_video = st.file_uploader("Upload Video", type = ['mp4','mpeg','mov'])
    if uploaded_video != None:
        
        vid = uploaded_video.name
        with open("uploaded_video.mp4", mode='wb') as f:
            f.write(uploaded_video.read()) # save video to disk

        st_video = open(vid,'rb')
        video_bytes = st_video.read()
        st.write("Uploaded Video:")
        st.video(video_bytes)
        #video_file = 'street.mp4'
        cap = cv2.VideoCapture(vid)
        _, image = cap.read()
        h, w = image.shape[:2]
        #out = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc#(*'avc3'), fps, insize)
        
        st.write("Output:")
        image_placeholder = st.empty()
        
        count = 0
        while True:
            _, image = cap.read()
            if _ != False:
                h, w = image.shape[:2]
                det_img,detections= fn.detect_from_image(image,"array")
                image_placeholder.image(det_img)

        os.remove("uploaded_video.mp4")

def main():
    new_title = '<p style="font-size: 42px;font-weight:bolder">Fire Detection System Using Image Processing</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)

    read_me = st.markdown("""
    This project was built using Streamlit and OpenCV 
    to demonstrate Fire detection in both videos(pre-recorded)
    and images.
    
    
    Fire detection is the main objective of this project besides surveillance. Fires are one of 
    the main causes of death amongst the world. Although there are various fire detection 
    systems most of them did not proof its effectiveness in detecting fires due to inefficiency 
    or restrictions. 

    The aim of the project is to early detection of fire apart from preventive measures to reduce 
    the losses due to hazardous fire."""
    )
    st.sidebar.title("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("About","Object Detection(Image)","Object Detection(Video)"))
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
    
    if choice == "Object Detection(Image)":
        #st.subheader("Object Detection")
        read_me_0.empty()
        read_me.empty()
        #st.title('Object Detection')
        object_detection_image()

    elif choice == "Object Detection(Video)":
        read_me_0.empty()
        read_me.empty()
        #object_detection_video.has_beenCalled = False
        #if object_detection_video.has_beenCalled:
        object_detection_video()
        

    elif choice == "About":
        print()
        

if __name__ == '__main__':
		main()	