#!/usr/bin/env python

# depending on your mod_wsgi configuration, you may need to uncomment these
# lines and adjust them as appropriate to make the relocations work:

# import os, sys
# sys.path.append('/var/www/atheme-web')
# os.chdir('/var/www/atheme-web')

def make_app(global_conf=None):
    from middleware.classpublisher import ClassPublisher
    from athemeweb.webroot import WebRoot
    real_app = ClassPublisher(WebRoot())

    from paste.exceptions.errormiddleware import ErrorMiddleware
    error_app = ErrorMiddleware(real_app, global_conf=global_conf)

    from paste.session import SessionMiddleware
    return SessionMiddleware(error_app)

application = make_app({'debug': True, 'expiration': 60})
