#
# Copyright (c) 2009 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

import threading
webinfo = threading.local()

from paste.request import parse_formvars
from paste.response import HeaderDict

class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.fields = parse_formvars(environ)

class Response(object):
    def __init__(self):
        self.headers = HeaderDict({'content-type': 'text/html'})
        self.status = "200 OK"

class ClassPublisher(object):
    def __init__(self, root):
        """
        Publish a class, making it capable to be URL traversed.

        For example, we want to convert /user/login to root.user.login().
        Or /channel/kickuser?victim=lol to root.channel.kickuser(victim='lol').
        """
        self.root = root

    def __call__(self, environ, start_response):
        webinfo.request = Request(environ)
        webinfo.response = Response()
        webinfo.environ = environ
        obj = self.find_object(self.root, environ)
        response_body = obj(**dict(webinfo.request.fields))
        start_response(webinfo.response.status, webinfo.response.headers.items())
        return [response_body]

    def find_object(self, obj, environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            # We've arrived!
            return obj

        # PATH_INFO always starts with a /, so we'll get rid of it:
        path_info = path_info.lstrip('/')

        # Then split the path into the "next" chunk, and everything
        # after it ("rest"):
        parts = path_info.split('/', 1)
        next = parts[0]

        if len(parts) == 1:
            rest = ''
        else:
            rest = '/' + parts[1]

        # Hide private methods/attributes:
        assert not next.startswith('_')

        # Now we get the attribute; getattr(a, 'b') is equivalent
        # to a.b...
        next_obj = getattr(obj, next)

        # Now fix up SCRIPT_NAME and PATH_INFO...
        environ['SCRIPT_NAME'] += '/' + next
        environ['PATH_INFO'] = rest

        # and now parse the remaining part of the URL...
        return self.find_object(next_obj, environ)

