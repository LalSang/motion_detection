# imported the OpenCV which gives us 
# webcam access, image windows, frame processing tools
import cv2 

# We set the variable vc to use our main webcam index which in this case 0
# 0 = "default camera"
# vc is now a live connection, not a frame
vc = cv2.VideoCapture(0)

# Here we are checking if the webcam opens 
# If not we throw an runtime error 
# If webcam don't open then raise an runtimeerror 
if not vc.isOpened():
    raise RuntimeError("Could not open webcam")

rval, frame = vc.read()
prev_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_grey = cv2.GaussianBlur(prev_grey, (21,21), 0)

# Here we are checking if webcam is reading frames 
# if not then we break 
while True:
    rval, frame = vc.read()
    if rval == False or frame == None:
        break 
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()
