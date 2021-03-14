# 舵机接线与驱动

标签（空格分隔）： davidben

---

#舵机与树莓派接线
接线图：http://shumeipai.nxez.com/2018/06/21/pan-tilt-multi-servo-control.html
在实际运用中，我将5V和GND接在树莓派上；BCM定义的引脚分别为17，27

树莓派GPIO引脚示意图，GPIO函数：http://shumeipai.nxez.com/2016/09/28/rpi-gpio-module-basics.html

#舵机驱动代码

舵机驱动代码使用到的基本树莓派GPIO操作函数：
按BCM模式定义引脚：

    GPIO.setmode(GPIO.BCM)

规定引脚和输入输出模式：

    GPIO.setup(channal,GPIO.IN)
    GPIO.steup(channal,GPIO.OUT)

servopin引脚的PWM波输出，p.start表示初始输入PWM波大小：

    p = GPIO.PWM(servopin,50)  #50HZ  
    p.start(0)   

改变PWM波输入
注意（个人试错）：大小写要严格遵守，不然会报错
有时候莫名报错，可以尝试重启代码

    p.ChangDutyCycle(4)
 
 值为4的PWM波持续时间：1s
 注意（网上教程常常没强调）：一定要加入这一行代码，同时设置时间不宜太短，否则舵机根本无法启动，或者无法达到要求的角度
 
    time.sleep(1)

 结束PWM波输出，同时清理引脚，释放资源：
 
    p.stop()
    GPIO.cleanup()

#舵机校准测试和转换公式建立

##校准测试代码

    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
      
    import RPi.GPIO as GPIO  
    import time  
    import signal  
    import atexit  
      
    atexit.register(GPIO.cleanup)    
      
    servopin = 17  
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(servopin, GPIO.OUT, initial=False)  
    p = GPIO.PWM(servopin,50) #50HZ  
    p.start(0)   
    p.ChangeDutyCycle(3)
    time.sleep(1)
    p.stop()
    GPIO.cleanup()
    
##SG90舵机校准
p.ChangeDutyCycle()中参数从3到14范围变化（这只是大致范围，对于每个舵机是不太一样的），记录每个参数对应的舵机角度
经过测试：
水平旋转舵机：参数3-14对应角度180-0
仰角舵机：参数2.6-11对应角度0-180（大致）

##角度与参数转换公式
水平旋转舵机
度数：0-180
参数：3-14

转化公式：pwm_x=error_x*0.0229+3
