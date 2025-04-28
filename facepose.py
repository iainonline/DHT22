# Iain McIntosh
# 4-4-2025
# MVP code to prove the concept of using a webcam to detect head pose
# This code uses the headpose library to detect head pose from a webcam image

import cv2
from headpose.detect import PoseEstimator
 
est = PoseEstimator()  #load the model

# create a loop that runs until the user presses the 'q' key
while True:
    # take an image using the webcam
    cam = cv2.VideoCapture(0)
    for i in range(cv2.CAP_PROP_FRAME_COUNT):
        cam.grab()
    ret, image = cam.retrieve()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # estimate the head pose
    # try to estimate the pose of the head in the image if exception occurs, print the exception and continue
    try:
        roll, pitch, yawn = est.pose_from_image(image)
    except Exception as e:
        print(e)
        continue
    
    # add roll, pitch, yawn to the image at the top left corner
    cv2.putText(image, f'roll: {roll:.2f}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(image, f'pitch: {pitch:.2f}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(image, f'yawn: {yawn:.2f}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
   
    # draw lines to split the image into 3 sections with vertical lines
    height, width = image.shape[:2]
    cv2.line(image, (width // 3, 0), (width // 3, height), (255, 255, 255), 1)
    cv2.line(image, (2 * width // 3, 0), (2 * width // 3, height), (255, 255, 255), 1)

    # display the image
    cv2.imshow('image', image)
    
    # save the image with a timestamp in the filename
    #timestamp = cv2.getTickCount()
    #filename = f'headpose_{timestamp}.jpg'
    #cv2.imwrite(filename, image)
    
    # if the user presses the 'q' key, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
