import cv2
import numpy as np
import requests

def detect_rats(url):
    # Load YOLOv5 model
    net = cv2.dnn.readNet('yolov5s.pt', 'yolov5s.cfg')
    classes = []
    with open('coco.names', 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    # Set camera URL
    cap = cv2.VideoCapture(url)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is available
        if not ret:
            break

        # Detect objects in the frame
        blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0)
        net.setInput(blob)
        outs = net.forward()

        # Extract bounding boxes and confidence scores
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply non-maximum suppression to remove overlapping boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Draw bounding boxes and labels on the frame
        for i in indices:
            i = i[0]
            box = boxes[i]
            x, y, w, h = box
            label = classes[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Rat Detection', frame)

        # Exit on ESC key press
        if cv2.waitKey(1) == 27:
            break

    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
