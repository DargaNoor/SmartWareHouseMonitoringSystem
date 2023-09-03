import wget

# Download the YOLOv5s model files from the official repository
url = 'https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt'
filename = 'yolov5s.pt'
wget.download(url, filename)

url = 'https://github.com/ultralytics/yolov5/raw/master/models/yolov5s.yaml'
filename = 'yolov5s.cfg'
wget.download(url, filename)
