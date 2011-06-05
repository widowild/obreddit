Description
-----------

Lets see your profile on the site [Reddit](http://www.reddit.com) with Menu [Openbox](http://openbox.org/)

Functionality
--------------

- Comment Karma Score
- Link Karma Score

Installation
------------

obreddit requires python3 and Openbox
Launch first a script
A file is created /home/<username>/.config/obreddit.conf
change a variable yourusername by a name profile
user = yourusername

Edit a openbox menu through [obmenu](http://obmenu.sourceforge.net/) and add pipemenu which point to the script
or Edit /home/<username>/.config/openbox/menu.xml
and add <menu execute="python /home/<username>/obreddit.py" id="pipe-xxxx" label="Reddit"/>

Licence
-------

GNU GENERAL PUBLIC LICENCE (GPL)