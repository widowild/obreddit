#!/usr/bin/env python

import os
import urllib.request
import configparser
import json
import sys

conf = os.environ['XDG_CONFIG_HOME'] + "/obreddit.conf"

if not os.path.isfile(conf): # test existence d'un fichier
    print("change your username in", conf)
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'User' : 'yourusername'}
    with open(conf, 'w') as configfile:
        config.write(configfile)

# lire fichier de configuration
config = configparser.ConfigParser()
config.read(conf)
user = config['DEFAULT']['User']

url = "http://www.reddit.com/user/" + user + "/about.json"
raw = urllib.request.urlopen(url).read().decode('utf-8')
data = json.loads(raw)['data']
#print data
karma = data['link_karma']
comment = data['comment_karma']

print('<openbox_pipe_menu>')
print('<separator label="User "/>')
print('<item label=\"%s\" />' % (user))
print('<separator label="Link Karma" />')
print('<item label=\"%s\" />' % (karma))
print('<separator label="Comment Karma" />')
print('<item label=\"%s\" />' % (comment))
print('</openbox_pipe_menu>')
