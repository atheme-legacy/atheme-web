#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from middleware.classpublisher import webinfo
from thirdparty.templite import Templite
from middleware.athemeconnection import AthemeXMLConnection
from athemeweb.config import XMLRPC_PATH

from urllib import quote_plus

def get_xmlrpc_connection():
    sessiondata = webinfo.environ['paste.session.factory']()
    conn = AthemeXMLConnection(XMLRPC_PATH)
    conn.username = sessiondata['conn.username']
    conn.authcookie = sessiondata['conn.authcookie']

    return conn

class ChannelRoot(object):
    def list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('mychannels_list').render(webinfo=webinfo, conn=conn)

    def info(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('channelinfo').render(webinfo=webinfo, conn=conn, channel=channel)

    def edit_flags(self, channel, nick=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('channeleditflags').render(webinfo=webinfo, conn=conn, channel=channel, nick=nick)

    def set_flags(self, channel, nick, flags):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.chanserv.set_access_flags(channel, nick, flags)
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'info?channel=' + quote_plus(channel)
        return ''

    def remove_flags(self, channel, nick):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.chanserv.set_access_flags(channel, nick, '-*fF')
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'info?channel=' + quote_plus(channel)
        return ''

    def info(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('channelinfo').render(webinfo=webinfo, conn=conn, channel=channel)

    def settings(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('channeleditsettings').render(webinfo=webinfo, conn=conn, channel=channel)

    def settings_commit(self, channel, TOPICLOCK='OFF', SECURE='OFF', FANTASY='OFF', RESTRICTED='OFF', VERBOSE_OPS='OFF', PRIVATE='OFF', KEEPTOPIC='OFF', GUARD='OFF', LIMITFLAGS='OFF', HOLD='OFF', VERBOSE='OFF'):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        if VERBOSE_OPS is True:
            VERBOSE = "OPS"

        conn.chanserv.set_channel_flag(channel, 'TOPICLOCK', TOPICLOCK)
        conn.chanserv.set_channel_flag(channel, 'SECURE', SECURE)
        conn.chanserv.set_channel_flag(channel, 'FANTASY', FANTASY)
        conn.chanserv.set_channel_flag(channel, 'RESTRICTED', RESTRICTED)
        conn.chanserv.set_channel_flag(channel, 'PRIVATE', PRIVATE)
        conn.chanserv.set_channel_flag(channel, 'KEEPTOPIC', KEEPTOPIC)
        conn.chanserv.set_channel_flag(channel, 'LIMITFLAGS', LIMITFLAGS)
        conn.chanserv.set_channel_flag(channel, 'VERBOSE', VERBOSE)

        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'settings'
        return ''

class MemoRoot(object):
    def delete_confirm(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.delete(id)
        return Templite('memodeleted').render(webinfo=webinfo, conn=conn, id=id)

    def delete(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memodelete').render(webinfo=webinfo, conn=conn, id=id)

    def read(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memoread').render(webinfo=webinfo, conn=conn, id=id)

    def list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memolist').render(webinfo=webinfo, conn=conn)

    def ignore_list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memoignores').render(webinfo=webinfo, conn=conn)

    def ignore_add(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memoignoreadd').render(webinfo=webinfo, conn=conn)

    def ignore_add_commit(self, account):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.ignore_add(account)
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'ignore_list'
        return ''

    def ignore_delete(self, account):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.ignore_delete(account)
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'ignore_list'
        return ''

    def ignore_clear(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.ignore_clear()
        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'ignore_list'
        return ''

    def write(self, to=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memowrite').render(webinfo=webinfo, conn=conn, to=to)        

    def write_commit(self, to, message):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.send(to, message)
        return Templite('memosent').render(webinfo=webinfo, conn=conn, to=to)

    def forward(self, id, to=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Templite('memoforward').render(webinfo=webinfo, conn=conn, message_id=id, to=to)

    def forward_commit(self, to, message_id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.forward(to, message_id)
        return Templite('memosent').render(webinfo=webinfo, conn=conn, to=to)

class UserRoot(object):
    def __init__(self):
        self.memo = MemoRoot()
        self.channel = ChannelRoot()

    def login(self):
        return Templite('userlogin').render()

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
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        return Templite('dashboard').render(webinfo=webinfo, conn=conn)

    def logout(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        conn.logout()
        sessiondata = webinfo.environ['paste.session.factory']()
        del sessiondata['conn.username']
        del sessiondata['conn.authcookie']

        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'login'
        return ''

    def account(self):
        return ''
