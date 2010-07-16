#
# Copyright (c) 2010 William Pitcock <nenolod@atheme.org>.
#
# This file is licensed under the Atheme license.
#

import os
from thirdparty.templite import Templite
from athemeweb.config import TEMPLATE_PATH, TEMPLATE_STYLE

class Template(Templite):
    def __init__(self, template):
        file = TEMPLATE_PATH + '/' + TEMPLATE_STYLE + '/' + template + '.tpl'
        if not os.path.exists(file):
            file = TEMPLATE_PATH + '/default/' + template + '.tpl'

        super(Template, self).__init__(file)

    def include(self, file, **kw):
        self.write(Template(file).render(kw))
