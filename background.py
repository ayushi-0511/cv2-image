
import cv2

# cap is capture
# this is my web cam
cap = cv2.VideoCapture(0)

#ret is reading the image, back = displays what it is capturing
while cap.isOpened():
    ret , back = cap.read() #HERE I AM READING FROM MY WEBCAM
    if ret: # if reading of image is successful then
        cv2.imshow("image" , back)
        if cv2.waitKey(5) == ord('q'):
            #save the image
            cv2.imwrite('image.jpg' , back)
            break


cap.release() # release all the resources
cv2.destroyAllWindows()
