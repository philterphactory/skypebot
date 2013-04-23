# coding=UTF-8

from string import Template
import rando

import pkgutil
import commands

from commandbase import BaseCommand

class WhutCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "cmd", "whut" ]
        
    def generate( self, name ):

        # import commands
        a_commands = []

        ## load all commands
        reload( commands )
        for loader, modname, ispkg in pkgutil.iter_modules( commands.__path__, prefix="commands." ):
        

            module = __import__( modname, fromlist="dummy" )
            reload( module )
            for klassname in dir( module ):
                if "Command" in klassname and "BaseCommand" not in klassname:
                    
                    
                    kommandklass = getattr( module, klassname )
                    kommand = kommandklass()
                    a_commands.append( kommand )
        out='commands: '
        for cmd in a_commands:
            l=cmd.command_mappings
            for c in l:
                out=out+c+' '
            
        message_out = out
        return "/me %s" % message_out
