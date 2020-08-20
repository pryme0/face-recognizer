'''
import numpy
import cv2
import os
face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
'cascades/data/haarcascade_frontal_alt2.xml'
cap = cv2.VideoCapture(0)

filename = 'video.avi' #avi,mp4
frames_per_secounds = 20
my_res = '480p'
#set resolution for the video capture
def change_res(cap,width,height):
	cap.set(3,width)
	cap.set(4,height)
#standard video dimension sizes
STD_DIMENSIONS ={

	"480p":(640,480),
	"720p":(1280,720),
	"1080p":(3840,1080),
	"4k":(3840,2160),
}
def get_dims(cap , res= '480p'):
	width,height = STD_DIMENSIONS['480p']
	if res in STD_DIMENSIONS:
		  width,height = STD_DIMENSIONS[res]
	change_res(cap,width,height)
	return width ,height
'''
'''def make_1080p():
	cap.set(3,1920)
	cap.set(4,1080)
def make_720p():
	cap.set(3,1280)
	cap.set(4,720)
def make_480p():
	cap.set(3,640)
	cap.set(4,480)
def change_res(width,height):
	cap.set(3,width)
	cap.set(4,height)
make_1080p()

def rescale_frame(frame, percent=75):
	scale_percent = 500
	width = int(frame.shape[1] * scale_percent/100)
	height = int(frame.shape[0] * scale_percent/100)
	dim = (width,height)
	return cv2.resize(frame,dim,interpolation= cv2.INTER_AREA)
	'''
'''
#video encoding

VIDEO_TYPE = {
	'avi':cv2.VideoWriter_fourcc(*'XVID'),
   # 'mp4':cv2.VideoWriter_fourcc(*'H264')
	'mp4':cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
	filename,ext = os.path.splitext(filename)

	if ext in VIDEO_TYPE:
		return VIDEO_TYPE[ext]
	return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
dims = get_dims(cap, res = my_res)
video_type_cv2 = get_video_type(filename)
out = cv2.VideoWriter(filename,video_type_cv2,frames_per_secounds,dims)

while True:
	#capture frame by frame
	ret, frame = cap.read()
	#change the color to gray
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
	for(x,y,w,h) in faces:
		print(x,y,w,h)
 # out.write(frame)
	#display the resulting frame
	out.write(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xff == ord('q'):
		break
#when everything is done,release the capture
cap.release()
out.release()
cv2.destroyAllWindows()

'''

import numpy as np
import cv2
import pickle
import datetime
import os

print("starting the software..........")

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
strTimename = ''
labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
#with open("log.txt","r+") as logfile:

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=1)
	f = open("log.txt", "r+")
	name_list = []
	for (x, y, w, h) in faces:
		#print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
		roi_color = frame[y:y+h, x:x+w]

		# recognize? deep learned model predict keras tensorflow pytorch scikit learn
		id_, conf = recognizer.predict(roi_gray)
		if conf>=47 and conf <= 82:
			print(conf)
			#print(5: #id_)
			#print(labels[id_])

			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			curTime = datetime.datetime.now()
			intconc =  int(conf)
			confi = 120 - intconc
			print (intconc)
			strTimename = name + " : " + str(curTime) + str(intconc)
			confid = name + str(confi) + "%"
			print(strTimename)
			color = (255, 255, 255)
			stroke = 2
			cv2.putText(frame, confid, (x,y), font, 1, color, stroke, cv2.LINE_AA)

		img_item = "7.png"
		cv2.imwrite(img_item, roi_color)
		color = (255, 0, 0) #BGR 0-255
		stroke = 2
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
		with open("log.txt","r") as file:
			content = file.read()
		with open("log.txt","a") as file:
			file.write(strTimename+"\n")
		#subitems = smile_cascade.detectMultiScale(roi_gray)
		#for (ex,ey,ew,eh) in subitems:
		#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
print(str(name_list))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



