#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from middleware.classpublisher import webinfo
from thirdparty.templite import Templite
from middleware.athemeconnection import AthemeXMLConnection
from athemeweb.config import XMLRPC_PATH

class UserRoot(object):
    def login(self):
        t = Templite('userlogin')
        return t.render()

    def process_login(self, nickname, password):
        webinfo.response.status = "302 Found"
        try:
            conn = AthemeXMLConnection(XMLRPC_PATH)
            conn.login(nickname, password)
        except:
            webinfo.response.headers['location'] = 'login'
            return ''

        webinfo.response.headers['location'] = 'dashboard'
        sessiondata = webinfo.environ['paste.session.factory']()
        sessiondata['conn.username'] = conn.username
        sessiondata['conn.authcookie'] = conn.authcookie
        return ''

    def dashboard(self):
        sessiondata = webinfo.environ['paste.session.factory']()
        try:
            conn = AthemeXMLConnection(XMLRPC_PATH)
            conn.username = sessiondata['conn.username']
            conn.authcookie = sessiondata['conn.authcookie']
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        t = Templite('dashboard')
        return t.render(webinfo=webinfo, conn=conn)
