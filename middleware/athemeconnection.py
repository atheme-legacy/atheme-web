#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from xmlrpclib import ServerProxy

class AthemeChanServMethods(object):
    """
    Parse Atheme ChanServ responses.  Since the XML interface provides the same output as the IRC interface, we
    have to do this.  It's kind of a pain in the ass.
    """
    def __init__(self, parent):
        self.parent = parent

    def kick(self, channel, victim, reason):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'KICK', channel, victim, reason)

class AthemeMemoServMethods(object):
    """
    Parse Atheme MemoServ responses.  Since the XML interface provides the same output as the IRC interface, we
    have to do this.  It's kind of a pain in the ass.
    """
    def __init__(self, parent):
        self.parent = parent

    def list(self):
        list = []

        data = self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'LIST')
        raw_lines = data.split('\n')

        for line in raw_lines:
            if line[0] != '-':
                continue

            data = line.split(' ', 5)
            tuple = {'from': data[3], 'sent': data[5]}

            list.append(tuple)

        return list

    def read(self, number):
        data = self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'READ', number)
        raw_lines = data.split('\n')

        fields = raw_lines[0].split(' ', 6)
        tuple = {'from': fields[5][0:-1], 'sent': fields[6], 'message': raw_lines[2]}

        return tuple

    def send(self, target, message):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'SEND', target, message)

    def send_ops(self, target, message):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'SENDOPS', target, message)

    def forward(self, target, message_id):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'FORWARD', target, message_id)

    def delete(self, message_id):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'DELETE', message_id)

    def ignore_add(self, target):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'IGNORE', 'ADD', target)

    def ignore_delete(self, target):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'IGNORE', 'DEL', target)

    def ignore_list(self):
        data = self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'IGNORE', 'LIST')
        raw_lines = data.split('\n')

        list = []
        for line in raw_lines:
            tuple = {}

            try:
                data = line.split(' ')
                tuple['id'] = int(data[0])
                tuple['account'] = data[2]
                list.append(tuple)
            except ValueError:
                continue

        return list

    def ignore_clear(self):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'MemoServ', 'IGNORE', 'CLEAR')

class AthemeXMLConnection(object):
    def __init__(self, url):
        self.proxy = ServerProxy(url)
        self.chanserv = AthemeChanServMethods(self)
        self.memoserv = AthemeMemoServMethods(self)

    def __getattr__(self, name):
        return self.proxy.__getattr__(name)

    def login(self, username, password):
        self.username = username
        self.authcookie = self.atheme.login(username, password)
