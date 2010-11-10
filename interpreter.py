from athemeweb.config import XMLRPC_PATH
from athemeweb.athemeconnection import AthemeXMLConnection
import code

x = AthemeXMLConnection(XMLRPC_PATH)
print "XMLRPC connection is declared as 'x'."
code.InteractiveConsole({'x': x}).interact()
