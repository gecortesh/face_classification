import cv2

camera = cv2.VideoCapture(0)

while (camera.isOpened()):
	ret, frame = camera.read()
	if not ret:
		print ("capture failed")
	cv2.imshow("", frame)
	if 0xff == ord("q"):
		break

camera.release()