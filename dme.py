import urllib2
import easygui
import os

"""
    Inspired from https://github.com/shrayasr/WgetHere
"""

msg = 'Inspired by Shrays-wget'
title = 'Enter the URL'
fieldNames = ['folder','URL']
f = easygui.multenterbox(msg,title,fieldNames)

if f[0] == '':
    mypath = 'c:/users/c_thv/desktop'
else:
    mypath = f[0]

fname =  f[1].split('/')[-1]
fullfilename = os.path.join(mypath,fname)

the_file = urllib2.urlopen(f[1])
output = open(fullfilename,'wb')
output.write(the_file.read())
output.close()
