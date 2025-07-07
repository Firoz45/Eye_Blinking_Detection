import cv2
import cvzone
from cvzone.FaceMeshModule import  FaceMeshDetector
from cvzone.PlotModule import LivePlot
cap = cv2.VideoCapture("E:\\Video\\python_project_Videos\\eye_blinking.mp4")
detector = FaceMeshDetector(maxFaces=1)

plotY =LivePlot(600,360,[20,50],invert=True)
idList =[22,23,24,26,110,157,158,159,160,161,130,243]
ratioList =[]
blinkCounter = 0
counter = 0
color = (0,200,0)
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) ==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()
    img,faces = detector.findFaceMesh(img, draw= False)

    if faces :
        face = faces[0]
        for id in idList:
            cv2.circle(img,face[id],5,color ,cv2.FILLED)
        leftUp = face[159]
        leftdown = face[23]
        leftLeft =face[130]
        leftRight =face[243]
        lengthVar,_= detector.findDistance(leftUp,leftdown)
        lengthHor,_ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img,leftUp,leftdown,(0,0,255),2)
        cv2.line(img, leftLeft, leftRight, (0, 0, 255), 2)
        ratio = (float(lengthVar/lengthHor)*100)
        ratioList.append(ratio)
        if len(ratioList)>3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList)/len(ratioList)

        if (ratioAvg< 31  and counter ==0):
            blinkCounter +=1
            color = (0,0,255)
            counter = 1
        if counter != 0:
            counter +=1
            if counter> 10:
                counter =0
                color = (0,200,0)

        cvzone.putTextRect(img,f'Blink Count: {blinkCounter}',(40,40),float (1.75), 2,
                          colorR=color )

        imgplot = plotY.update(ratioAvg,color)
        cv2.imshow("ImagePlot",imgplot)
        img = cv2.resize(img, (600, 360))
        imgStack = cvzone.stackImages([img,imgplot],2, float(0.9))
    else:
        img = cv2.resize(img, (600, 360))
        imgStack = cvzone.stackImages([img, img], 2,  float(0.90))
    cv2.imshow("BlinkingImageResult",imgStack)
    cv2.waitKey(25)