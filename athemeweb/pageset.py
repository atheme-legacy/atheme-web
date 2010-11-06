#
# Copyright (c) 2010 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

def build_page_set(conn):
    pageset = {
        'account': {
            'title': "My Account",
            'privs': None
        },
        'channel/list': {
            'title': "My Channels",
            'privs': None
        },
        'memo/list': {
            'title': "My Memos",
            'privs': None
        },
        'akill/list': {
            'title': "AKILLs",
            'privs': 'operserv:akill',
        },
        'logout': {
            'title': "Logout",
            'privs': None
        },
    }

    realset = {}
    for i in pageset.keys():
        page = pageset[i]
        if page['privs'] is None or (conn is not None and conn.has_privilege(page['privs'])):
            realset[i] = page

    return realset

if __name__ == '__main__':
    from config import XMLRPC_PATH
    from athemeconnection import AthemeXMLConnection

    x = AthemeXMLConnection(XMLRPC_PATH)
    x.login('someuser', 'somepass')

    from pprint import pprint
    pprint(build_page_set(x))
