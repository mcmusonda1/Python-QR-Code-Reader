import cv2

check = cv2.QRCodeDetector()
test, points, straight_qrcode = check.detectAndDecode(cv2.imread(input("Enter your QR Code you want to be read: \n")))

print(test)