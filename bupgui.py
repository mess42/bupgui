#!/usr/bin/env/python
"""
bupgui is a primitive gui for the commandline backup bup. 

Copyright (C) 2015 Moritz Esslinger moritz.esslinger@web.de

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


#include <batteries.h>
from Tkinter import *
import sys, os
import getpass

class bupgui(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.displayinit = False
        self.pack()
        self.createWidgets()
        
        self.scriptdir = str(os.path.realpath(__file__))
        self.scriptdir = self.scriptdir.replace(str(os.path.basename(__file__)).strip(), "")
        self.bupdir    = self.scriptdir + "bupdir"

    def createWidgets(self):
        self.savebutton = Button( self, text="Save /home/"+getpass.getuser(), command=self.bupsave )
        self.savebutton.grid(row=0, column=0, columnspan=1)
        self.viewbutton = Button( self, text="View Backups", command=self.viewbackups )
        self.viewbutton.grid(row=1, column=0, columnspan=1)

    def bupsave(self):
        os.system( "bup -d " + self.bupdir + " index -u ~/" )
        os.system( "bup -d " + self.bupdir + " save -n backup_" + getpass.getuser() + " ~/" )

    def viewbackups(self):
        #fusermount -u 
        os.system("bup -d " + self.bupdir + " fuse " + self.scriptdir + "mountpoint")
        os.system("xdg-open " + self.scriptdir + "mountpoint")
 
root = Tk()
root.title( "simple bup gui" )
app = bupgui(master = root )
app.mainloop()
