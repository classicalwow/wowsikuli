import time

import random

#第一步 1920*1080 缩放1
#第二步 设置英语打字
i = 0;
while True:
    
    if exists("1566912124291.png",0):
        click("1566912173905.png");
        time.sleep(20);

    elif exists("1570671525847.png",0):
        click("1570671525847.png")
        time.sleep(5)
    elif exists("1566912201827.png",0):
        click("1570627425420.png");
        time.sleep(5)
    elif exists("1570627544862.png",0):
        click("1570627537523.png")
        time.sleep(20)
    
    else:
        time.sleep(random.randrange(40,80));
        print "我擦"
        click(Location(10, 10));
        time.sleep(1);
        if(i%2==0): 
            keyDown(Key.UP)
            time.sleep(0.5);
            keyUp(Key.UP)
        else:
            keyDown(Key.DOWN)
            time.sleep(0.5);
            keyUp(Key.DOWN)
        i=i+1;