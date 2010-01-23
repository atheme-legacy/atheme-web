#!/usr/bin/env python

import sys

def make_app(global_conf=None):
    from middleware.classpublisher import ClassPublisher
    from athemeweb.webroot import WebRoot
    real_app = ClassPublisher(WebRoot())

    from paste.exceptions.errormiddleware import ErrorMiddleware
    error_app = ErrorMiddleware(real_app, global_conf=global_conf)

    from paste.session import SessionMiddleware
    return SessionMiddleware(error_app, global_conf=global_conf)

if __name__ == '__main__':
    from paste import httpserver
    if len(sys.argv) == 2:
        if sys.argv[1] == '--debug':
            httpserver.serve(make_app({'debug': True, 'expiration': 60}), host='0.0.0.0', port='8080')
        else:
            httpserver.serve(make_app({'debug': False, 'expiration': 60}), host='0.0.0.0', port='8080')
