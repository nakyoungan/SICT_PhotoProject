import cv2
from PIL import Image


#동영상에서 사진 찍는
cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1080)
fc = 20.0
codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
out = cv2.VideoWriter('mycam.avi', codec, fc, (int(cap.get(3)), int(cap.get(4))))
while True:
    ret, frame = cap.read()
    cv2.imshow('test', frame)
    out.write(frame)
    k = cv2.waitKey(1)

    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite('save_image.jpg', frame)

        break

    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()

result_width = 800
result_height = 2700

input_path_1 = r'C:\Users\USER\PycharmProjects\SICTPhotoProject\save_image.jpg' # 덮어쓸 사진의 경로
result = Image.new("L",(result_width, result_height))
input_img_1 = Image.open(r'C:\Users\USER\PycharmProjects\SICTPhotoProject\save_image.jpg')
result.paste(im=input_img_1, box=(80, 80)) # 1번째 사진 덮어쓰기
result.paste(im=input_img_1, box=(80, 640)) # 2번째 사진 덮어쓰기
result.paste(im=input_img_1, box=(80, 1200)) # 3번째 사진 덮어쓰기
result.paste(im=input_img_1, box=(80, 1760)) # 4번째 사진 덮어쓰기

result.save(r'C:\Users\USER\PycharmProjects\SICTPhotoProject\result_image.jpg') # 사진이 저장될 경로