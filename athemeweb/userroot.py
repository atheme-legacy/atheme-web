#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from athemeweb.classpublisher import webinfo
from athemeweb.template import Template
from athemeweb.athemeconnection import AthemeXMLConnection
from athemeweb.config import XMLRPC_PATH

from urllib import quote_plus

def get_xmlrpc_connection():
    sessiondata = webinfo.environ['paste.session.factory']()
    conn = AthemeXMLConnection(XMLRPC_PATH, webinfo.environ['REMOTE_ADDR'])
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

        return Template('mychannels_list').render(webinfo=webinfo, conn=conn)

    def info(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('channelinfo').render(webinfo=webinfo, conn=conn, channel=channel)

    def edit_flags(self, channel, nick=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('channeleditflags').render(webinfo=webinfo, conn=conn, channel=channel, nick=nick)

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

        return Template('channelinfo').render(webinfo=webinfo, conn=conn, channel=channel)

    def settings(self, channel):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('channeleditsettings').render(webinfo=webinfo, conn=conn, channel=channel)

    def settings_commit(self, channel, TOPICLOCK='OFF', SECURE='OFF', FANTASY='OFF', RESTRICTED='OFF', VERBOSE_OPS='OFF', PRIVATE='OFF', KEEPTOPIC='OFF', GUARD='OFF', LIMITFLAGS='OFF', HOLD='OFF', VERBOSE='OFF'):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        if VERBOSE_OPS is True:
            VERBOSE = "OPS"

        params = {
            'TOPICLOCK': TOPICLOCK,
            'SECURE': SECURE,
            'FANTASY': FANTASY,
            'RESTRICTED': RESTRICTED,
            'PRIVATE': PRIVATE,
            'KEEPTOPIC': KEEPTOPIC,
            'LIMITFLAGS': LIMITFLAGS,
            'VERBOSE': VERBOSE,
        }

        for key in params.keys():
            try:
                conn.chanserv.set_channel_flag(channel, key, params[key])
            except:
                pass

        webinfo.response.status = "302 Found"
        webinfo.response.headers['location'] = 'settings?channel=%s' % quote_plus(channel)
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
        return Template('memodeleted').render(webinfo=webinfo, conn=conn, id=id)

    def delete(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('memodelete').render(webinfo=webinfo, conn=conn, id=id)

    def read(self, id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('memoread').render(webinfo=webinfo, conn=conn, id=id)

    def list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('memolist').render(webinfo=webinfo, conn=conn)

    def ignore_list(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('memoignores').render(webinfo=webinfo, conn=conn)

    def ignore_add(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('memoignoreadd').render(webinfo=webinfo, conn=conn)

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

        return Template('memowrite').render(webinfo=webinfo, conn=conn, to=to)        

    def write_commit(self, to, message):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.send(to, message)
        return Template('memosent').render(webinfo=webinfo, conn=conn, to=to)

    def forward(self, id, to=''):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        return Template('memoforward').render(webinfo=webinfo, conn=conn, message_id=id, to=to)

    def forward_commit(self, to, message_id):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = '/user/login'
            return ''

        conn.memoserv.forward(to, message_id)
        return Template('memosent').render(webinfo=webinfo, conn=conn, to=to)

class UserRoot(object):
    def __init__(self):
        self.memo = MemoRoot()
        self.channel = ChannelRoot()

    def login(self):
        return Template('userlogin').render()

    def process_login(self, nickname, password):
        webinfo.response.status = "302 Found"
        try:
            conn = AthemeXMLConnection(XMLRPC_PATH)
            conn.login(nickname, password)
        except:
            webinfo.response.headers['location'] = 'login'
            return ''

        webinfo.response.headers['location'] = 'account'
        sessiondata = webinfo.environ['paste.session.factory']()
        sessiondata['conn.username'] = conn.username
        sessiondata['conn.authcookie'] = conn.authcookie
        return ''

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

    def update_password(self, new_password):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        conn.nickserv.set_password(new_password)

        webinfo.response.headers['refresh'] = '5; URL=account'
        return Template('genericmessage').render(webinfo=webinfo, conn=conn, message='Your password has been set to %s' % new_password)

    def update_email(self, new_email):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        conn.nickserv.set_email(new_email)

        webinfo.response.headers['refresh'] = '5; URL=account'
        return Template('genericmessage').render(webinfo=webinfo, conn=conn, message='Your e-mail has been set to %s' % new_email)

    def account(self):
        try:
            conn = get_xmlrpc_connection()
        except:
            webinfo.response.status = "302 Found"
            webinfo.response.headers['location'] = 'login'
            return ''

        return Template('userinfo').render(webinfo=webinfo, conn=conn)
