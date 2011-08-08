#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from athemeweb.userroot import UserRoot
from athemeweb.classpublisher import webinfo

class StaticRoot(object):
    def __getattr__(self, attr):
        def reader(*a):
            fd = open('./static/'+attr)
            return fd.read()
        return reader

class WebRoot(object):
    def __call__(self):
        webinfo.response.status = "302 Redirect"
        webinfo.response.headers['location'] = "/user/login"
        return ''

    def __init__(self):
        self.user = UserRoot()

    static = StaticRoot()
