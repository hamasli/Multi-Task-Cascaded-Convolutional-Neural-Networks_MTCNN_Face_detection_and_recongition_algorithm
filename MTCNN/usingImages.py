from mtcnn import MTCNN;
import cv2;
import tensorflow as tf;

detector=MTCNN();
img=cv2.imread('images/img_3.png');
#for single object;
# output=detector.detect_faces(img);
# print(output);
# x1,y1,w,h=output[0]['box'];
#
# lefteX,lefteY=output[0]['keypoints']['left_eye'];
# righteX,righteY=output[0]['keypoints']['right_eye'];
# noseX,noseY=output[0]['keypoints']['nose'];
# mouthlX,mouthlY=output[0]['keypoints']['mouth_left'];
# mouthrX,mouthrY=output[0]['keypoints']['mouth_right']
# cv2.circle(img,(lefteX,lefteY),color=(0,0,255),thickness=2,radius=2);
# cv2.circle(img,(righteX,righteY),color=(0,0,255),thickness=2,radius=2);
# cv2.circle(img,(noseX,noseY),color=(0,0,255),thickness=2,radius=2);
# cv2.circle(img,(mouthlX,mouthlY),color=(0,0,255),thickness=2,radius=2);
# cv2.circle(img,(mouthrX,mouthrY),color=(0,0,255),thickness=2,radius=2);
# cv2.rectangle(img,(x1,y1),(w+x1,h+y1),color=(0,255,0),thickness=2);
# cv2.imshow("image",img);
# cv2.waitKey(0);

#using multiple objects in single image
output=detector.detect_faces(img);
for i in output:

    x1, y1, w, h = i['box'];
    lefteX, lefteY = i['keypoints']['left_eye'];
    righteX,righteY=i['keypoints']['right_eye'];
    noseX,noseY=i['keypoints']['nose'];
    mouthlX,mouthlY=i['keypoints']['mouth_left'];
    mouthrX,mouthrY=i['keypoints']['mouth_right']
    cv2.circle(img,(lefteX,lefteY),color=(0,0,255),thickness=2,radius=1);
    cv2.circle(img,(righteX,righteY),color=(0,0,255),thickness=2,radius=1);
    cv2.circle(img,(noseX,noseY),color=(0,0,255),thickness=2,radius=1);
    cv2.circle(img,(mouthlX,mouthlY),color=(0,0,255),thickness=2,radius=1);
    cv2.circle(img,(mouthrX,mouthrY),color=(0,0,255),thickness=2,radius=1);
    cv2.rectangle(img,(x1,y1),(w+x1,h+y1),color=(0,255,0),thickness=2);
cv2.imshow("image",img);
cv2.waitKey(0);


