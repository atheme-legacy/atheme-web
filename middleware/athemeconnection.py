#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

from xmlrpclib import ServerProxy

class AthemeNickServMethods(object):
    """
    Parse Atheme NickServ responses.  Since the XML interface provides the same output as the IRC interface, we
    have to do this.  It's kind of a pain in the ass.
    """
    def __init__(self, parent):
        self.parent = parent
        self.flags = ['Hold', 'HideMail', 'NeverOp', 'NoOp', 'NoMemo', 'EMailMemos', 'Private']

    def _parse_access(self, data):
        raw_lines = data.split('\n')

        list = []
        for line in raw_lines:
            fields = line.split(' ')

            if fields[0] != 'Access':
                continue

            tuple = {'channel': fields[4], 'flags': fields[2]}
            list.append(tuple)

        return list

    def list_own_access(self):
        return self._parse_access(self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'NickServ', 'MYACCESS'))

    def list_access(self, target):
        return self._parse_access(self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'NickServ', 'LISTCHANS', target))

    def get_info(self, target):
        data = self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'NickServ', 'INFO', target)
        raw_lines = data.split('\n')

        tuple = {}
        for line in raw_lines:
            if "Information on" in line:
                continue
            if ":" not in line:
                continue

            fields = line.split(':', 1)
            tuple[fields[0].strip()] = fields[1].strip()

        return tuple

    def get_account_flags(self, target):
        data = self.get_info(target)
        flags = data['Flags']

        tuple = {}
        for flag in self.flags:
            if flag in flags:
                tuple[flag] = True
            else:
                tuple[flag] = False

        return tuple

    def set_password(self, password):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'NickServ', 'SET', 'PASSWORD', password)

    def set_email(self, email):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'NickServ', 'SET', 'EMAIL', email)

class AthemeChanServMethods(object):
    """
    Parse Atheme ChanServ responses.  Since the XML interface provides the same output as the IRC interface, we
    have to do this.  It's kind of a pain in the ass.
    """
    def __init__(self, parent):
        self.parent = parent
        self.flags = ['HOLD', 'SECURE', 'VERBOSE', 'VERBOSE_OPS', 'RESTRICTED', 'KEEPTOPIC', 'TOPICLOCK', 'GUARD', 'FANTASY', 'PRIVATE', 'LIMITFLAGS']

    def kick(self, channel, victim, reason):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'KICK', channel, victim, reason)

    def get_access_list(self, channel):
        data = self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'FLAGS', channel)
        raw_lines = data.split('\n')

        list = []
        for line in raw_lines:
            tuple = {}

            try:
                data = line.split(None, 3)
                tuple['id'] = int(data[0])
                tuple['nick'] = data[1]
                tuple['flags'] = data[2]
                list.append(tuple)
            except ValueError:
                continue

        return list

    def get_access_flags(self, channel, nick):
        return self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'FLAGS', channel, nick)

    def set_access_flags(self, channel, nick, flags):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'FLAGS', channel, nick, '=' + flags)

    def get_channel_info(self, channel):
        data = self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'INFO', channel)
        raw_lines = data.split('\n')

        tuple = {}
        for line in raw_lines:
            if line[0] == '*' or "Information on" in line:
                continue

            fields = line.split(' : ', 2)
            tuple[fields[0].strip()] = fields[1].strip()

        return tuple

    def get_channel_flags(self, channel):
        data = self.get_channel_info(channel)
        flags = data['Flags']

        tuple = {}
        for flag in self.flags:
            if flag in flags:
                tuple[flag] = True
            else:
                tuple[flag] = False

        return tuple

    def set_channel_flag(self, channel, flag, value):
        self.parent.atheme.command(self.parent.authcookie, self.parent.username, '0.0.0.0', 'ChanServ', 'SET', channel, flag, value)

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
        self.nickserv = AthemeNickServMethods(self)

    def __getattr__(self, name):
        return self.proxy.__getattr__(name)

    def login(self, username, password):
        self.username = username
        self.authcookie = self.atheme.login(username, password)

    def logout(self):
        self.atheme.logout(self.authcookie, self.username)
