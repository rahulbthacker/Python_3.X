#!/usr/bin/python

'''
When we download songs from the Internet, the naming convention is pretty messed up. If we want to listen to a playlist, the order is mixed, which is inconvenient. Using Python's 'os' module, we can help ease this problem.
'''

import os

os.chdir('Path/')

for each in os.listdir():
    each_name, each_extension = os.path.splitext(each)

    each_song, each_album, each_number = each_name.split('-')

    each_song = each_song.strip()
    each_album = each_album.strip()
    each_number = each_number.strip()[2:].zfill(2)

    final_list = '{}-{}-{}{}'.format(each_number, each_song, each_album, each_extension)
    os.rename(each, final_list)
