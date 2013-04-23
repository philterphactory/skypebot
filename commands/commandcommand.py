# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

import pkgutil
import commands

class CommandCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "command", "cmd", "whut" ]
        
    def generate( self, name ):

        command_list=[]
        # import commands
        all_commands = []

        ## load all commands
        reload( commands )
        for loader, modname, ispkg in pkgutil.iter_modules( commands.__path__, prefix="commands." ):
        

            module = __import__( modname, fromlist="dummy" )
            reload( module )
            for klassname in dir( module ):
                if "Command" in klassname and "BaseCommand" not in klassname:
                    
                    
                    kommandklass = getattr( module, klassname )
                    kommand = kommandklass()
                    all_commands.append( kommand )
        out='commands: '
        for cmd in all_commands:
            l=cmd.command_mappings
            for c in l:
                out=out+c+' '
            
        message_out = out
        return "/me %s" % message_out
