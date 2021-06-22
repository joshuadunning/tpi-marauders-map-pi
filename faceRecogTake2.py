import cv2
cap = cv2.VideoCapture("rtsp://TheCamera:Password@10.80.0.20/live")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
