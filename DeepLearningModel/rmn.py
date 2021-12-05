# # from IPython.display import Image

# import cv2
# from rmn import RMN


# # Image('image.jpg', width=400)
# m = RMN()

# # image = cv2.imread("C:\\Users\\User\\Documents\\zoom_project\\DeepLearningModel\\5.jpg")
# image = cv2.imread("C:\\Users\\User\\Desktop\\image.jpg")
# results = m.detect_emotion_for_single_frame(image)

# # print(results[0])
# person1 = results[0]
# print(results[0])
# person2 = results[1]
# person3 = results[2]
# person4 = results[3]
# person5 = results[4]
# person6 = results[5]
# person7 = results[6]
# print(person1['emo_label'])
# print(person2['emo_label'])
# print(person3['emo_label'])
# print(person4['emo_label'])
# print(person5['emo_label'])
# print(person6['emo_label'])
# print(person7['emo_label'])


# from IPython.display import Image
import cv2
from rmn import RMN
#streamlit library
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from ast import literal_eval
#제목   
st.title('Emotion Control')
hour_to_filter = st.slider('Person Number', 1, 7, 1)
checkbox_btn = st.checkbox("Show your Data")
if checkbox_btn: 
    st.write("Data Loaded")
    #캡쳐 이미지 출력
    from PIL import Image
    image = Image.open('5.jpg')
   
    st.image(image)
    
    # Image('image.jpg', width=400)
    m = RMN()

    image = cv2.imread("5.jpg")
    results = m.detect_emotion_for_single_frame(image)


   

    
    #그대로 출력
    # st.write(person1['emo_label'])
    # st.write(person2['emo_label'])
    # st.write(person3['emo_label'])
    # st.write(person4['emo_label'])
    # st.write(person5['emo_label'])
    # st.write(person6['emo_label'])
    # st.write(person7['emo_label'])

    #딕셔러니
    # st.write("<Chart>")
    # dict_2 = {} # blank Dictionary
    # dict_2['person1'] = person1['emo_label']
    # dict_2['person2'] = person2['emo_label']
    # dict_2['person3'] = person3['emo_label']
    # dict_2['person4'] = person4['emo_label']
    # dict_2['person5'] = person5['emo_label']
    # dict_2['person6'] = person6['emo_label']
    # dict_2['person7'] = person7['emo_label']
    # person = dict_2
    # st.write((person))


    # sample = {person1['emo_label'],person2['emo_label'],person3['emo_label'],person4['emo_label'],person5['emo_label']
    # ,person6['emo_label'],person7['emo_label']}


    # data1 = pd.DataFrame({
    # 'person': ['1', '2', '3','4','5','6','7'],
    # 'emotion': [person1['emo_label'],person2['emo_label'],person3['emo_label'],person4['emo_label'],person5['emo_label']
    # ,person6['emo_label'],person7['emo_label']],
    # })

    personList = [];
    # print(results[0])
    person1 = results[0]
    person2 = results[1]
    person3 = results[2]
    person4 = results[3]
    person5 = results[4]
    person6 = results[5]
    person7 = results[6]

    personList.append(person1);
    personList.append(person2);
    personList.append(person3);
    personList.append(person4);
    personList.append(person5);
    personList.append(person6);
    personList.append(person7)


    neutral = 0;
    angry = 0;
    disgust = 0;
    fear = 0;
    happy = 0;
    sad = 0;
    surprise = 0;
    understand = 0;
    misunderstsand = 0;

    for person in personList:
        if person['emo_label'] == "neutral":
            neutral += 1;
            understand += 1;
        elif person['emo_label'] == "angry":
            angry += 1;
            misunderstsand += 1;
        elif person['emo_label'] == "disgust":
            disgust += 1;
            misunderstsand += 1;
        elif person['emo_label'] == "fear":
            fear += 1;
            misunderstsand += 1;
        elif person['emo_label'] == "happy":
            happy += 1;
            understand += 1;
        elif person['emo_label'] == "sad":
            sad += 1;
            misunderstsand += 1;
        elif person['emo_label'] == "surprise":
            surprise += 1;
            misunderstsand += 1;
        else: break



    data1 = pd.DataFrame({
    'emotion': ['neutral', 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise'],
    'amount': [neutral, angry, disgust, fear, happy, sad, surprise],
    })








    checkbox_btn2 = st.checkbox("View Chart")
    if checkbox_btn2:
        st.write(data1) 
        st.write(alt.Chart(data1,width=3,height=7).mark_bar().encode(
        x=alt.X('emotion', sort=None),
        y='amount',
        ))

    # st.info("Information - The results don't tell you everything.")
