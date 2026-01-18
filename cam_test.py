# imported the OpenCV which gives us 
# webcam access, image windows, frame processing tools
import cv2 

# We set the variable vc to use our main webcam index which in this case 0
# 0 = "default camera"
# vc is now a live connection, not a frame
vc = cv2.VideoCapture(0)
MIN_AREA = 1500
# Here we are checking if the webcam opens 
# If not we throw an runtime error 
# If webcam don't open then raise an runtimeerror 
if not vc.isOpened():
    raise RuntimeError("Could not open webcam")

rval, frame = vc.read()
if not rval or frame is None:
    raise RuntimeError("Could not read initial frame")
prev_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_grey = cv2.GaussianBlur(prev_grey, (21,21), 0)

# Here we are checking if webcam is reading frames 
# if not then we break 
while True:
    motion_found = False

    rval, frame = vc.read()
    if rval == False:
        break 
    # Compute Motion Difference
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    # compute absolute difference between frames
    # diff -> threshold -> dilate -> erode 
    # detect movement, Make movement areas solid, Clean up the result 
    diff = cv2.absdiff(prev_grey, gray)

    # threshold the difference image
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = cv2.erode(thresh, None, iterations=1)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for c in contours:
        if cv2.contourArea(c) < MIN_AREA:
            motion_found = True
            continue

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if motion_found:
        cv2.putText(frame,"Motion", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255),2,cv2.LINE_AA)
    else:
        cv2.putText(frame,"No Motion", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2, cv2.LINE_AA)

    # show motion mask
    cv2.imshow("motion", thresh)
    # update reference frame 
    prev_grey = gray

    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == ord('q'):
        break


vc.release()
cv2.destroyAllWindows()
