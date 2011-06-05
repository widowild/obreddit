#!/usr/bin/env python3
#
# obreddit [version 0.1]
#
# Copyright 2010 Wido <widomaker2k7@gmail.com>
# Distributed under the terms of the GNU General Public License v3.
# See http://www.gnu.org/licenses/gpl.txt for the full license text.
#
# Depends : Openbox and Python 3
#
# lets see your profile on the site http://www.reddit.com with Menu Openbox
#
# Change your username in /home/$USER/.config/obreddit.conf
# add pipemenu in your menu and add action for example
# python /your_folder/obreddit.py

import os
import urllib.request
import configparser
import json
import time
import sys

conf = os.environ['XDG_CONFIG_HOME'] + "/obreddit.conf"

if not os.path.isfile(conf):
    print("change your username in", conf)
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'User' : 'yourusername'}
    with open(conf, 'w') as configfile:
        config.write(configfile)

# read configuration file
config = configparser.ConfigParser()
config.read(conf)
user = config['DEFAULT']['User']

url = "http://www.reddit.com/user/" + user + "/about.json"
raw = urllib.request.urlopen(url).read().decode('utf-8')
data = json.loads(raw)['data']
karma = data['link_karma']
comment = data['comment_karma']
created = data['created_utc']

print('<openbox_pipe_menu>')
print('<separator label="User"/>')
print('<item label=\"%s\" />' % (user))
print('<separator label="Redditor since"/>')
print('<item label=\"%s\" />' % (time.ctime(created)))
print('<separator label="Link Karma" />')
print('<item label=\"%s\" />' % (karma))
print('<separator label="Comment Karma" />')
print('<item label=\"%s\" />' % (comment))
print('</openbox_pipe_menu>')
