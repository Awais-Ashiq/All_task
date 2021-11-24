# Image proccessing and text extration techniques in python
[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/vt5fpE0bzSY)
 In this repository you can find most valuable method to learn and persue forward in profesional career.
 there are different things being done in the repository and working tree is mentioned bellow

 ## Task 1
  ### Model 1 | PyTesseract
Text extration using optical character recogition written in python library named as PyTesseract.
this library is based on the OCR model and it helps in finding text from an image.
But you need to give some preprocessing stuf in image to make it compatible with the model for text reading.
Because most of the models can not give accurate result on exact image we have to filter images out by using 
different preprocessing techniques. 

 ### Model 2 | EasyOCR
This is other text  Extration python library that is used to fetch data from image using OCR.
this library does not require image preproccesing because it does it by it self and give back some results.

 ### Model 3 | East Model 
Is just like OCR but it returns Bounding boxes only like it will just detect the text.

## Task 2
 ### opencv-python
In this module we have manipulate some basic operations of opencv-python in which we have done 
image rotation flipping  sliding croping resizing and many other image related tasks.
we have done normal image preprocessing techniques like image rotation, translation, fliping.
 
 ### Pillow | MetaData | NumPy
This library is much like opencv but it has some minur changer like cv2 convert image into array but pillow takes image as it is. and it reads in RGB format. pillow library also work with meta data and manipulatees it by using different 
methos.
## Task 3
 ### OCR with Flask
In this project we have done text detection using flask API. this time it is done on runtime not on images.

to work with this Projects you have to follow some simple steps
requirements needed to work with this Project.
First of all you need to have python on your machine
and then clone the repository by following this command
but you need to be in the same directory as you are working while 
runing the below mentioned command in terminal
so follow commands step by step

```bash  
git clone https://github.com/Awais-Ashiq/flask_ocr.git
cd flask_ocr/Flask_Ocr_online
```
And then run this command
```bash  
pip install -r requirements.txt
```
Above mentioned command will install all the required files to run your application.
now we will discus some features of this application.
in this app what you have to do is you have to run the following command
in the terminal
```bash  
python3 app.py
```
Now your server is up and running. and now copy the following command to run the
applications in browser.
http://127.0.0.1:5000/
above mentioend url is the local servers url this will host your application until the 
is shutdown.
now a layout will be displayed in front of the browser

![App Screenshot](https://i.ibb.co/vBzHvwv/flask-ocr-online.png)

Now in order to scan your id card and extract information you have to click on open camera
button. 
when you click on the open camera button a new box will appear inside the 
browser to open the default or any external attached camera installed on you system.
here it will look like this.

![App Screenshot](https://i.ibb.co/1dD6SgL/camera-open.png)

    as you can see in above mentioned screen shot i am going to scan my id card infront
    of the camera. 
    now pressthe close camera button to close the camera and begin processing
    the text extraction. nwo it take some time and my your video screen
    will pause for some may for 5 to 8 minutes depends on the quality of video
    when the desired data got extracted then browser will move to hoem page
    and print the result in table format as mentioend bellow.

    ![App Screenshot](https://i.ibb.co/WHq4TgX/results-of-ocr.png)


    ## Authors

    - [@Muhammad Awais](https://github.com/Awais-Ashiq)



## 🛠 Skills
- Deep learning
- Python
- OCR



         