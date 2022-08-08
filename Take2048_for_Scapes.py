# -*- encoding=utf8 -*-
__author__ = "PC-23"

from airtest.core.api import *
from datetime import datetime, date, time

auto_setup(__file__)
def TakeScreenshot():
    curDTObj = datetime.now()
    snapshot(r"C:/Users/PC-23/Documents/AirTest_report/%s.jpg" %curDTObj.strftime("%H %M %S %f"), quality=99, max_size=1400)
def DetectTaskMenu():
    if exists(Template(r"tpl1659955596782.png", record_pos=(-0.009, 0.946), resolution=(1080, 2220)) and Template(r"tpl1659955611215.png", record_pos=(0.306, 0.636), resolution=(1080, 2220))):
        
        touch(Template(r"tpl1659955643066.png", record_pos=(0.303, 0.639), resolution=(1080, 2220)))
        sleep(1)
        
def StartTask():
    if exists(Template(r"tpl1659958163189.png", record_pos=(-0.004, -0.557), resolution=(1080, 2220)) and Template(r"tpl1659958180284.png", record_pos=(0.169, -0.168), resolution=(1080, 2220))):
        TakeScreenshot()
    touch(Template(r"tpl1659958198033.png", record_pos=(0.159, -0.171), resolution=(1080, 2220)))
    sleep(6)
    TakeScreenshot()
    Wheel()
    
def Wheel():
    if exists(Template(r"tpl1659958378634.png", record_pos=(0.003, 0.192), resolution=(1080, 2220))):
        touch(Template(r"tpl1659958402393.png", record_pos=(0.37, -0.946), resolution=(1080, 2220)))
        sleep(1)
        TakeScreenshot()
        DetectTaskMenu()
        CompletedLocation()
        
    
        
def CompletedLocation():
    if exists(Template(r"tpl1659958475120.png", record_pos=(-0.009, -0.362), resolution=(1080, 2220)) and Template(r"tpl1659958487462.png", record_pos=(0.006, 0.255), resolution=(1080, 2220))):
        touch(Template(r"tpl1659958502741.png", record_pos=(0.005, 0.251), resolution=(1080, 2220)))
        sleep(2)
     
    else: sleep(1)
 

for x in range (0, 10000):
    DetectTaskMenu()
    StartTask()
    
  