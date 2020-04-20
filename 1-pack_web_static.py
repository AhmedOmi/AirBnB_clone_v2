#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz
archive from the contents of the web_static folder of
your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    print(date)
    local("sudo mkdir versions")
    print(local)
    directory = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static/".format(directory))
    return directory
