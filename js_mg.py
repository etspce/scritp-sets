import cv2
import json

f = open('./mg/000000050323_2d.json', 'r')
data = f.read()
a = json.loads(data)

img_path = '000000050323(1).jpg'
img = cv2.imread(img_path)  # 读取图片

for i in range(len(a['predicted_2d'])):
    # print(int(a['predicted_2d'][i][0]), int(a['predicted_2d'][i][1]))
    cv2.circle(img, (int(a['predicted_2d'][i][0]), int(a['predicted_2d'][i][1])), 3, (0, 255, 0), -1)
    # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
    # cv2.circle(输入的图片data,圆心位置,圆的半径,圆的颜色,圆形轮廓的粗细（如果为正）负数(-1)表示要绘制实心圆,圆边界的类型,中心坐标和半径值中的小数位数)

cv2.imshow('img', img)
# 写出图片
cv2.imwrite("000000050323_hl.jpg", img)
