import cv2;
from mtcnn import MTCNN;
cap=cv2.VideoCapture(0);
detector=MTCNN();


while True:
    success,img=cap.read();
    output=detector.detect_faces(img);
    for i in output:
        x1,y1,w,h=i['box'];
        lefteX, lefteY = i['keypoints']['left_eye'];
        righteX, righteY = i['keypoints']['right_eye'];
        noseX, noseY = i['keypoints']['nose'];
        mouthlX, mouthlY = i['keypoints']['mouth_left'];
        mouthrX, mouthrY = i['keypoints']['mouth_right']
        cv2.circle(img, (lefteX, lefteY), color=(0, 0, 255), thickness=2, radius=1);
        cv2.circle(img, (righteX, righteY), color=(0, 0, 255), thickness=2, radius=1);
        cv2.circle(img, (noseX, noseY), color=(0, 0, 255), thickness=2, radius=1);
        cv2.circle(img, (mouthlX, mouthlY), color=(0, 0, 255), thickness=2, radius=1);
        cv2.circle(img, (mouthrX, mouthrY), color=(0, 0, 255), thickness=2, radius=1);
        cv2.rectangle(img, (x1, y1), (w + x1, h + y1), color=(0, 255, 0), thickness=2);



    cv2.imshow("frame",img);
    cv2.waitKey(1);