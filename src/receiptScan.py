import cv2
import pytesseract
import numpy 

class Scan:

  totalWords = ('total', 'amount', 'payment', 'subtotal', 'payment', 'due')

  def __init__(self):
    # create a blank image
    self.receipt = numpy.zeros((500, 500, 3), dtype='uint8')


  def captureImage(self):
    cam = cv2.VideoCapture(0)
    cam.set(10,500) # sets the brightness
    cv2.namedWindow("Receipt Scanner")

    while True:
      success, frame = cam.read()
      if not success:
        print("Webcam Failed")
        break

      cv2.imshow("Receipt Scanner", frame)

      k = cv2.waitKey(1)
      if k % 256 == 32: # captures the image when the spacebar is pressed
        img = "scan.jpg"
        cv2.imwrite(img, frame)
        print("Scan complete")
        break

    cam.release()
    cv2.destroyAllWindows()
    return
    


  def processImage(self):
    img = cv2.imread("scan.jpg")
    # convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # make the image bigger
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    # add a bilateral filter
    img = cv2.bilateralFilter(img, 9, 3, 3)
    # binarize the image
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,15)
    # dilate text
    img = cv2.erode(img, (5,5), iterations=1)
    self.receipt = img
    return


  def isfloat(self, num):
    try:
        float(num)
        return True
    except ValueError:
        return False


  def findTotal(self):
    receiptData = pytesseract.image_to_string(self.receipt)
    details = list(receiptData.split())
    total = -1.0
    found = False
    for i in range(len(details)):
      details[i] = details[i].lower()
      if '$' in details[i]:
        details[i]=details[i].replace('$','')
      if found:
        if self.isfloat(details[i]):
          total = max(total, float(details[i]))
          found = False
      if details[i] in self.totalWords:
        found = True

    return total

  