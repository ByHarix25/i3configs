import os, random as rd
#starts xmobar if there is not an instance of it already running
def startxmobar():
    print('Starting xmobar...')
    if (os.system('ps -e | grep xmobar') == 256):
        os.system('xmobar')
        print('xmobar started successfully')
        pass
    print('xmobar is already running')

#This is personal, I have an HD tv that I use as a monitor and when I connect it, it updates the resolution automatically
os.system('xrandr --output HDMI-A-0 --auto')
os.system('xrandr --output HDMI-A-0 --same-as eDP')
if (os.system('xrandr --current | grep \'HDMI-A-0 connected\' > /dev/null') != 256):
    os.system('xrandr --output eDP --scale-from 1280x720 > /dev/null')
    print('Successfully changed resolution')
else:
    print('A monitor could not be found. Keeping the same resolution')
    os.system('xrandr --output eDP --scale-from 1920x1080 > /dev/null')

filedir = os.path.dirname(os.path.realpath(__file__))
#Sees if there is a "bg" folder in the folder the file is in
if not os.path.exists(f'{filedir}/bg/'):
#If it does not find one, it tries to create one
    print('[WARN] Directory \"bg\" could not be found. Creating one')
    try:
        os.system(f'mkdir {filedir}/bg')
    except:
        #If it fails to create one because of a lack of permissions or any other reason, it tries to run xmobar and exits 
        print('[ERROR] Not enough permissions to create folder \"bg\". Skipping')
        startxmobar()
        exit()

#bg random chooser
size = int(os.popen(f'ls {filedir}/bg | wc -l').read())
if size == 0:
    print('[WARN] No backgrounds in the "bg" folder. Skipping')
    startxmobar()
    exit()
#Assign global variable with the number of background
else:
    os.system(f'export CUSTOMBG={size}')
bgnum = rd.randint(1, size)

#Try to find the background selected randomly that ends in .jpg or .png
try:
    os.system(f'exec feh --no-fehbg --bg-scale {filedir}/bg/bg{bgnum}.jpg')
except:
    try:
        os.system(f'exec feh --no-fehbg --bg-scale {filedir}/bg/bg{bgnum}.png')
    except:
        #If a variant could not be found, it cycles through all the possible files until it finds one that works
        print('[ERROR] The selected background has the wrong file format! Please use .png or .jpg\nTrying to find a background')
        for x in size:
            try:
                os.system(f'exec feh --no-fehbg --bg-scale {filedir}/bg/bg{bgnum}.jpg')
            except:
                try:
                     os.system(f'exec feh --no-fehbg --bg-scale {filedir}/bg/bg{bgnum}.png')
                except:
                    pass
        #If it does not find any background, it quits and calls to start xmobar
        print('Could not find any background. Skipping')
startxmobar()


