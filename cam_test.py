# imported the OpenCV which gives us 
# webcam access, image windows, frame processing tools
import cv2 

# We set the variable vc to use our main webcam index which in this case 0
# 0 = "default camera"
# vc is now a live connection, not a frame
vc = cv2.VideoCapture(0)

# Here we are checking if the webcam opens 
# If not we throw an runtime error 
# if vc.isOpened():
#     rval = True
# else:
#     rval = False
#     raise RuntimeError("Could not open webcam")

# If webcam don't open then raise an runtimeerror 
if not vc.isOpened():
    raise RuntimeError("Could not open webcam")

while True:
    rval, frame = vc.read()
    cv2.imshow("preview", frame)

    if rval == False or frame == None:
        exit 
    
