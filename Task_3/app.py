from flask import Flask, render_template, Response
from camera import Video, TextDetection, OpenVideo
from datetime import datetime
import cv2
close_cam = True
app = Flask(__name__)

def generate_cam(camera):
    global close_cam
    while close_cam:
        ret, frame = camera.get_frame()
        if not ret:
            break
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.cam_releaser()
    # print('-----------------------------')

@app.route('/')
def index():
    global close_cam
    close_cam = True
    return render_template('index.html')


@app.route('/videopage')
def videopage():
    return render_template('video.html')


@app.route('/video')
def video():

    return Response(generate_cam(Video('static/videos/output.avi')), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/closecam')
def closecam():
    personal = {'name': '-',
            'father name': '-',
            'identity number': '-',
            'gender': '-',
            'dates': []
            }
    global close_cam
    close_cam = False
    dates = []
    is_filled = True
    face_cascade = cv2.CascadeClassifier(
        'model/haarcascade_frontalface_default.xml')
    vid = OpenVideo('static/videos/output.avi')

    saved = False
    while not saved:
        ret, frame = vid.read_video()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        box, detection = face_cascade.detectMultiScale2(
            gray, minNeighbors=8)  # Face Detection
        if len(detection)>0:
            for x, y, w, h in box:
                img = frame[y-30:y+h+30, x-30:x+w+30]
                saved = cv2.imwrite('static/images/prof.jpg', img)

    vid = TextDetection('static/videos/output.avi')
    count = 0
    while is_filled:
        ret, frame = vid.get_video().read()
        if not ret:
            break
        if count %10 == 0:
            results = vid.process(frame)
        elif count == 600:
            break
        count += 1
        
        for index in range(1, len(results)):
            print(results[index][1])
            if (results[index][1] not in personal.values()) and (results[index][2] > .9):
                if ('-' not in personal.values() and len(personal['dates']) == 3):
                    is_filled = False
                    break
                elif str(results[index][1]) == 'Name':
                    personal['name'] = results[index+1][1]
                elif str(results[index][1]) == 'Father Name':
                    personal['father name'] = results[index+1][1]
                elif str(results[index][1]).count('-')==2 and (results[index][1] not in personal.values()) and len(results[index][1])==15:
                    personal['identity number'] = results[index][1]
                elif 'm' == str(results[index][1]).lower():
                    personal['gender'] = 'M'
                elif 'f' == str(results[index][1]).lower():
                    personal['gender'] = 'F'
                elif results[index][1].count('.')==2 and (str(results[index][1]) not in personal['dates']) and (results[index][2] > .95):
                    personal['dates'].append(results[index][1])
            print(personal)
    dates = [datetime.strptime(x, '%d.%m.%Y') for x in personal['dates']]
    dates.sort()
    personal['dates'] = [x.strftime('%d-%b-%Y') for x in dates]

    return render_template('index.html', personal=personal)


if __name__ == "__main__":
    app.run(debug=True)
