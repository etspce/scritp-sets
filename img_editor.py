import cv2

img_path = "1.jpg"
img = cv2.imread(img_path)  # 读取图片

cv2.circle(img, (100, 100), 10, (0, 0, 0), -1)
# cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
# cv2.circle(输入的图片data,圆心位置,圆的半径,圆的颜色,圆形轮廓的粗细（如果为正）负数(-1)表示要绘制实心圆,圆边界的类型,中心坐标和半径值中的小数位数)

cv2.imshow('img', img)

# 画框
cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 0), 1)
# cv2.rectangle(图片,矩形左上角的坐标位置,矩形右下角的坐标位置,颜色,线的粗细)

# 写出图片
cv2.imwrite("D:/PyQt5/4.jpg", img)
