import cv2
import numpy as np
import dlib
import threading
import time

ageProto="/root/Project Metro/Models/age_deploy.prototxt"
ageModel="/root/Project Metro/Models/age_net.caffemodel"
genderProto="/root/Project Metro/Models/gender_deploy.prototxt"
genderModel="/root/Project Metro/Models/gender_net.caffemodel"
MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-3)', '(4-6)', '(8-15)', '(15-18)', '(18-25)', '(30-45)', '(48-55)', '(60-100)']
genderList=['Male','Female']
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)
face_detector = cv2.CascadeClassifier("/root/Project Metro/Models/haarcascade_frontalface_default.xml")

OUTPUT_SIZE_WIDTH = 1280
OUTPUT_SIZE_HEIGHT = 650


rectangleColor = (0,165,255)

def doRecognizePerson(faceNames, fid):
	time.sleep(2)
	faceNames[ fid ] = "Person " + str(fid)


def run(videoName):


	detect_interval = 1
	scale_rate = 0.7
	show_rate = 1
	colours = np.random.rand(32, 3)
	count=0	
	
	frameCounter = 0
	currentFaceID = 0
	faceTrackers = {}
	faceNames = {}

	webcam = cv2.VideoCapture(videoName)
	fps = webcam.get(cv2.CAP_PROP_FPS)

	if fps==0:
		print("No Input Stream Detected")
		webcam.release()
		cv2.destroyAllWindows()
		return 

	if not webcam.isOpened():
		print("No Input Stream Detected")
		webcam.release()
		cv2.destroyAllWindows()
		return 

	while(webcam.isOpened()):

		status, frame = webcam.read()	
		baseImage = cv2.resize(frame, ( 320, 240))

		if not status:
			print("Could not read frame")
			webcam.release()
			cv2.destroyAllWindows()
			return 

		resultImage = baseImage.copy()
		frameCounter += 1 
		
		fidsToDelete = []
		for fid in faceTrackers.keys():
			trackingQuality = faceTrackers[ fid ].update( baseImage )

			if trackingQuality < 7:
				fidsToDelete.append( fid )
	
		for fid in fidsToDelete:
			print("Removing fid " + str(fid) + " from list of trackers")
			faceTrackers.pop( fid , None )

		if (frameCounter % 10) == 0:
	
			gray = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)
			
			faces = face_detector.detectMultiScale(gray, 1.3, 5)

			
			for (_x,_y,_w,_h) in faces:
				x = int(_x)
				y = int(_y)
				w = int(_w)
				h = int(_h)
				
				x_bar = x + 0.5 * w
				y_bar = y + 0.5 * h

				matchedFid = None

				for fid in faceTrackers.keys():
					tracked_position =  faceTrackers[fid].get_position()

					t_x = int(tracked_position.left())
					t_y = int(tracked_position.top())
					t_w = int(tracked_position.width())
					t_h = int(tracked_position.height())
				
					t_x_bar = t_x + 0.5 * t_w
					t_y_bar = t_y + 0.5 * t_h

					if ((t_x<=x_bar<=(t_x+t_w))and(t_y<=y_bar<=(t_y+t_h))and(x<=t_x_bar<=(x+w))and(y<=t_y_bar<=(y+h))):

						matchedFid = fid

				if matchedFid is None:

					print("Creating new tracker " + str(currentFaceID))

                        		#Create and store the tracker 
					tracker = dlib.correlation_tracker()
					
					tracker.start_track(baseImage,dlib.rectangle( x-10,y-20,x+w+10,y+h+20))

					faceTrackers[ currentFaceID ] = tracker

					t = threading.Thread( target = doRecognizePerson,args=(faceNames, currentFaceID))
					t.start()

					currentFaceID += 1

		for fid in faceTrackers.keys():

			tracked_position =  faceTrackers[fid].get_position()

			t_x = int(tracked_position.left())
			t_y = int(tracked_position.top())
			t_w = int(tracked_position.width())
			t_h = int(tracked_position.height())
						
			if fid not in faceNames.keys():
		
				face=baseImage[t_y:t_h,t_x:t_w]

				blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
				genderNet.setInput(blob)
				genderPreds=genderNet.forward()
				gender=genderList[genderPreds[0].argmax()]
				print('Person :',count+1)
				print(f'Gender: {gender}')
				ageNet.setInput(blob)
				agePreds=ageNet.forward()
				age=ageList[agePreds[0].argmax()]
				print(f'Age: {age[1:-1]} years')
	
	             
				count+=1
	                
				cv2.imwrite("{0}/{1}{2}_{3}.jpg".format("facepics",gender,age,fid),face)

			cv2.rectangle(resultImage, (t_x, t_y),(t_x + t_w , t_y + t_h),rectangleColor ,2)
						
			cv2.putText(resultImage, f'{gender}, {age}', (t_x, t_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)

			largeResult = cv2.resize(resultImage,(OUTPUT_SIZE_WIDTH,OUTPUT_SIZE_HEIGHT))

			cv2.imshow("Detecting age and gender", largeResult)

		if cv2.waitKey(1) & 0XFF == ord('q'):
			print("Detection Stopped Manually")
			webcam.release()
			cv2.destroyAllWindows()
			return 
			break
			


