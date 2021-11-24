import cv2
import easyocr

class Video(object):
    def __init__(self,  path) -> None:
        self.video = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.path = path
        self.cam = cv2.VideoWriter(self.path, fourcc, 20.0, (640,480))
    def __del__(self):
        self.video.release()
        self.cam.release()
    def get_frame(self):
        ret, frame = self.video.read()
        self.cam.write(frame)
        ret, jpg = cv2.imencode('.jpg', frame)
        return ret,jpg.tobytes()
    def get_obj(self):
        return self.cam
    def cam_releaser(self):
        if self.video.isOpened():
            return self.video.release()
    def is_open(self):
        return self.video.isOpened()


class TextDetection(object):
    reader = easyocr.Reader(['en'])
    def __init__(self,path):
        self.path = path
        self.video = cv2.VideoCapture(self.path)
    
    def get_video(self):
        return self.video
    def __del__(self):
        self.video.release()
    def process(self, frame):
        self.frame = frame
        return self.reader.readtext(self.frame)

class OpenVideo(object):
    def __init__(self, path):
        self.path = path
        self.video = cv2.VideoCapture(path)
    def __del__(self):
        self.video.release()
    def read_video(self):
        return self.video.read()
    def is_open(self):
        return self.video.isOpened()