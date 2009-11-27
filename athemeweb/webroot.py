#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from athemeweb.userroot import UserRoot
from middleware.classpublisher import webinfo

class WebRoot(object):
    def __call__(self):
        webinfo.response.status = "302 Redirect"
        webinfo.response.headers['location'] = "/user/login"
        return ''

    def __init__(self):
        self.user = UserRoot()

    def static(self, file):
        fd = open('./static/' + file)
        return fd.read() 
