import cv2
import numpy as np
import os

# 1. Load Model and Labels
net = cv2.dnn.readNet("../model/yolov3.weights", "../model/yolov3.cfg")
classes = []
with open("../model/names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
colors = np.random.uniform(0, 255, (len(classes),3)) # Generate random colors with 3 channels

# 2. Extract Final Layer
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

# 3. Load Sample Image
path = "../images/"
img = cv2.imread(path + os.listdir(path)[0])
height, width, channels = img.shape

# 4. Create Blob and Pass Into The Network
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, False)
net.setInput(blob)
outs = net.forward(output_layers)

# 5. Display Detected Images
class_ids = []
boxes = []
confidences = []

for out in outs:
    for info in out:
        scores = info[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence>0.5:
            center_x = int(info[0] * width)
            center_y = int(info[1] * height)
            w = int(info[2] * width)
            h = int(info[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
confidences = [round(num, 4) for num in confidences]

print(len(indexes), "objects detected")

for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]]) + "(" + str(confidences[i]) + ")"
        color = (42, 42, 165)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x-10, y - 25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()