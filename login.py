# import streamlit as st
# import cv2
# import numpy as np
# import os
# import time
# from st_pages import Page, show_pages, add_page_title, hide_pages

# add_page_title()
# st.header('카메라를 바라봐주세요.')
# show_pages(
#     [
#         Page("login.py", "Login", "🔐"),
#         Page("페이지1.py", "페이지1"),
#         Page("페이지2.py", "페이지2"),
#         Page("페이지3.py", "페이지3"),
#         Page("페이지4.py", "페이지4"),
#         Page("ecosaver.py", "main"),
#     ]
# )
# hide_pages(["페이지1",'페이지2','페이지3','페이지4','main'])

# # with st.spinner('잠시만 기다려주세요'):
# #     time.sleep(5)

# data_path = '../Facial-Recognition/faces/'
# onlyfiles = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path,f))]

# Training_Data, Labels = [], []

# for i, files in enumerate(onlyfiles):
#     image_path = os.path.join(data_path, onlyfiles[i])
#     images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     Training_Data.append(np.asarray(images, dtype=np.uint8))
#     Labels.append(i)

# Labels = np.asarray(Labels, dtype=np.int32)

# model = cv2.face.LBPHFaceRecognizer_create()

# model.train(np.asarray(Training_Data), np.asarray(Labels))

# print("Model Training Complete!!!!!")

# face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# def face_detector(img, size=0.5):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray, 1.3, 5)

#     if faces is ():
#         return img, []

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
#         roi = img[y:y + h, x:x + w]
#         roi = cv2.resize(roi, (200, 200))

#     return img, roi

# cap = cv2.VideoCapture(0)
# stframe = st.empty()

# while True:
#     img_file_buffer = st.camera_input("Take a picture")
#     if img_file_buffer is not None:
#         bytes_data = img_file_buffer.getvalue()
#         frame = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#     else:
#         ret, frame = cap.read()

#     image, face = face_detector(frame)

#     try:
#         face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#         result = model.predict(face)

#         if result[1] < 500:
#             confidence = int(100 * (1 - (result[1]) / 300))
#             display_string = str(confidence) + '% Confidence it is user'
#         cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)

#         if confidence > 75:
#             cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
#             break
#         else:
#             cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

#         stframe.image(image, channels="BGR")

#     except:
#         cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

#         stframe.image(image, channels="BGR")

#     if cv2.waitKey(1) == 13:
#         break

# cap.release()
# cv2.destroyAllWindows()

# with st.spinner('Wait for it...'):
#     time.sleep(5)

# if confidence > 85:
#     st.header("로그인 성공!")
#     st.page_link("ecosaver.py", label="메인페이지 이동", icon="1️⃣")
#     # hide_pages(["Login"])
# else:
#     st.header("로그인 실패!")
#     st.text('새로고침을 통해 다시 시도해주세요!')

import streamlit as st
import cv2
import numpy as np
import os
import time
from st_pages import Page, show_pages, add_page_title, hide_pages

add_page_title()
st.header('카메라를 바라봐주세요.', divider='rainbow')
st.subheader('깜빡임까지 약 5초정도 소요됩니다.')
show_pages(
    [
        Page("login.py", "Login", "🔐"),
        Page("페이지1.py", "페이지1"),
        Page("페이지2.py", "페이지2"),
        Page("페이지3.py", "페이지3"),
        Page("페이지4.py", "페이지4"),
        Page("ecosaver.py", "main"),
    ]
)
hide_pages(["페이지1",'페이지2','페이지3','페이지4','main'])

# with st.spinner('잠시만 기다려주세요'):
#     time.sleep(5)

data_path = '../Facial-Recognition/faces/'
onlyfiles = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path,f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))

    return img, roi

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100 * (1 - (result[1]) / 300))
            display_string = str(confidence) + '%'
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)

        if confidence > 85:
            cv2.putText(image, "Success", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            
        else:
            cv2.putText(image, "Fail", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        break
        # cv2.imshow('Face Cropper', image)
    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Face Cropper', image)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

# with st.spinner('잠시만 기다려 주세요...'):
#     time.sleep(5)

if confidence > 85:
    st.header("✅로그인 성공!")
    st.image(image, use_column_width=False)
    st.page_link("ecosaver.py", label="메인페이지 이동", icon="1️⃣")
    # hide_pages(["Login"])
elif confidence <= 85:
    st.header("❌로그인 실패!")
    st.text('새로고침을 통해 다시 시도해주세요!')
    st.image(image, use_column_width=False)
    # st.image(image, use_column_width=True)