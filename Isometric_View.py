import pyautogui as p
import time 
import subprocess
#subprocess.call('C:\Windows\System32\mspaint.exe')
time.sleep(15)
p.moveTo(730,708,duration=1)
p.dragRel(0,-200,duration=0.5)
p.dragRel(173,-100,duration=0.5)
p.dragRel(0,200,duration=0.5)
p.dragRel(-173,100,duration=0.5)

p.dragRel(0,-200,duration=0.5)
p.dragRel(-173,-100,duration=0.5)
p.dragRel(0,200,duration=0.5)
p.dragRel(173,100,duration=0.5)

p.dragRel(0,-200,duration=0.5)
p.dragRel(173,-100,duration=0.5)
p.dragRel(-173,-100,duration=0.5)
p.dragRel(-173,100,duration=0.5)
