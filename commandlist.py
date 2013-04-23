import time
import pkgutil
import datetime
import json
import sys
import logging
import twitterconnector
from hookserver import HookServerMessage, HookServerThread
import queuedthread
import time
from messages import housekeeping, streetnoise
import re
import os
import commands
import urllib2
import urllib

command_list=[]
        # import commands
all_commands = []
logging.info( "Loading commands..." )
        ## load all commands
reload( commands )
for loader, modname, ispkg in pkgutil.iter_modules( commands.__path__, prefix="commands." ):
    try:
        logging.info( "Scan module: %s" % modname)
        module = __import__( modname, fromlist="dummy" )
        reload( module )
        for klassname in dir( module ):
            if "Command" in klassname and "BaseCommand" not in klassname:
                logging.info( "...instantiate command: %s" % klassname )
                try:
                    kommandklass = getattr( module, klassname )
                    kommand = kommandklass()
                    all_commands.append( kommand )
                    logging.info( "......instantiated. Triggers are %s" % kommand.command_mappings )
                except Exception, e:
                    logging.info( e )    
    except Exception, e:
        logging.info( e )
    global command_list
    command_list=all_commands

out='commands: '
for cmd in all_commands:
    l=cmd.command_mappings
    for c in l:
        out=out+c+' '

print out

