#!/usr/bin/env python

def make_app(global_conf=None):
    from middleware.classpublisher import ClassPublisher
    from athemeweb.webroot import WebRoot
    real_app = ClassPublisher(WebRoot())

    from paste.exceptions.errormiddleware import ErrorMiddleware
    error_app = ErrorMiddleware(real_app, global_conf=global_conf)

    from paste.session import SessionMiddleware
    return SessionMiddleware(error_app)

application = make_app({'debug': True})
