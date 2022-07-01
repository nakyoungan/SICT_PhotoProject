import cv2
import time
import os
from PIL import Image

print('스융네컷 가즈아')

#동영상에서 사진 찍는
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 720)
cap.set(4, 1080)
fc = 20.0
codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
out = cv2.VideoWriter('mycam.avi', codec, fc, (int(cap.get(3)), int(cap.get(4))))

n = 1
while True:
    ret, frame = cap.read()
    cv2.imshow('test', frame)
    out.write(frame)
    k = cv2.waitKey(5)

    if (n == 5):
        break
    if k == ord('q'):
        cv2.imwrite('save_image' + str(n) + '.jpg', frame)
        print(str(n) + '번째 사진')
        n += 1

    if k == 27:
        break

result_width = 800
result_height = 2700

#result = Image.new("L", (result_width, result_height))
result = Image.open('./damgom.jpg') # 프레임

input_img_1 = Image.open('./save_image1.jpg') # 덮어쓸 사진의 경로
input_img_2 = Image.open('./save_image2.jpg') # 덮어쓸 사진의 경로
input_img_3 = Image.open('./save_image3.jpg') # 덮어쓸 사진의 경로
input_img_4 = Image.open('./save_image4.jpg') # 덮어쓸 사진의 경로

result.paste(im=input_img_1, box=(80, 264))
result.paste(im=input_img_2, box=(80, 798))
result.paste(im=input_img_3, box=(80, 1332))
result.paste(im=input_img_4, box=(80, 1866))


result_count = 0

while(1):
    if(not(os.path.isfile('./result_image'+ str(result_count) + '.jpg'))):
        print('./result_image'+ str(result_count) + '.jpg')
        result.save('./result_image'+ str(result_count) + '.jpg') # 사진이 저장될 경로
        break
    else:
        result_count += 1
        print("Result : " + str(result_count))

cap.release()
cv2.destroyAllWindows()