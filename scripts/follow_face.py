from __future__ import division
import cv2
        
import RPi.GPIO as GPIO  
import time  
import signal  
import atexit
        
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
face_cascade = cv2.CascadeClassifier( '123.xml' ) 

P=1 
I=0
D=0
        
thiserror_x=0
lasterror_x=0
thiserror_y=0
lasterror_y=0
error_x=0
error_y=0
pwm_x=0
outx=0
x=0
y=0
        
while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )
        max_face = 0
        value_x = 0
        if len(faces)>0:
            print('face found!')
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)
                result = (x,y,w,h)
                x=result[0]
                y=result[1]
                

        thiserror_x=x-240
        avr_x=thiserror_x*P+(thiserror_x-lasterror_x)*D+lasterror_x*I
        avr_x=thiserror_x*P+(thiserror_x-lasterror_x)*D+lasterror_x*I
        lasterror_x=thiserror_x
                    
        error_x=480-(avr_x+240)
        pwm_x=error_x*0.0229+3
        print(pwm_x)
        #print(outx)
        print(x)
        print(error_x)
          
        atexit.register(GPIO.cleanup)    
      
        servopin = 17  
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(servopin, GPIO.OUT, initial=False)  
        p = GPIO.PWM(servopin,50) #50HZ  
        p.start(0)   
        p.ChangeDutyCycle(pwm_x)
        time.sleep(0.1)
        p.stop()
        GPIO.cleanup()    
        
        cv2.imshow("capture", frame)
        outx=240-x
        outy=160-y
        if outx<10 and outx>-10 and outy<10 and outy>10:
            cv2.imwrite('face.jpg',frame)
            print('completed')
            
        if cv2.waitKey(1)==119:
            break

cap.release()
cv2.destroyAllWindows()