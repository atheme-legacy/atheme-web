#
# Copyright (c) 2010 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

def build_page_set(conn):
    pageset = [
        {
            'path': 'account',
            'title': "My Account",
            'privs': None
        },
        {
            'path': 'channel/list',
            'title': "My Channels",
            'privs': None
        },
        {
            'path': 'memo/list',
            'title': "My Memos",
            'privs': None
        },
        {
            'path': 'akill/list',
            'title': "AKILLs",
            'privs': 'operserv:akill',
        },
    ]

    realset = []
    for page in pageset:
        if page['privs'] is None or (conn is not None and conn.has_privilege(page['privs'])):
            realset.append(page)

    return realset

if __name__ == '__main__':
    from config import XMLRPC_PATH
    from athemeconnection import AthemeXMLConnection

    x = AthemeXMLConnection(XMLRPC_PATH)
    x.login('someuser', 'somepass')

    from pprint import pprint
    pprint(build_page_set(x))
