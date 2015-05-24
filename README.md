# bupgui

bupgui is a primitive GUI for the commandline backup tool bup.
It does not support any settings, and thus cannot be used in a wrong way by inexperienced users.

It saves the home folder of the user executing it.



How to install and configure:

!/bin/bash

sudo apt-get install python-tk bup

sudo usermod -aG fuse $USER

cp bupgui.py /media/backupdrive

cd /media/backupdrive

mkdir bupdir

mkdir mountpoint

bup -d bupdir init

python /media/backupdrive/bupgui.py
