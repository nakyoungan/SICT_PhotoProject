import cv2 as cv

#cap = cv.VideoCapture(0)
cap = cv.VideoCapture(0, cv.CAP_DSHOW)  #동영상 입력 부분을 관리하는 함수

while cap.isOpened():   #if Video Captured prepared
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("프로그램이 프레임을 수신하지 않움!") #Can't receive frame (stream end?). Exiting
        break

    # Display the resulting frame
    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q'):
        cv.imwrite("sict.jpg", frame)
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()