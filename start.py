import os, random as rd
os.system('xrandr --output HDMI-A-0 --auto')
os.system('xrandr --output HDMI-A-0 --same-as eDP')
if (os.system('xrandr --current | grep \'HDMI-A-0 connected\' > /dev/null') != 256):
  os.system('xrandr --output eDP --scale-from 1280x720 > /dev/null')
  print('Successfully changed resolution')
else:
  print('Could not change resolution')
  os.system('xrandr --output eDP --scale-from 1920x1080 > /dev/null')
#bg random chooser
size = int(os.popen('ls $HOME/.config/bg | wc -l').read())
bgnum = rd.randint(1, size)

os.system(f'exec feh --no-fehbg --bg-scale $HOME/.config/bg/bg{bgnum}.jpg')
if (os.system('ps -e | grep xmobar') == 256):
    os.system('xmobar')

