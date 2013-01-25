# coding=UTF-8

from string import Template
import random
import commands
import pkgutil
import logging
from commandbase import BaseCommand

class HelpCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "help" ] 


                            
    def generate( self, name ):

        s=' '.join(all_commands)
        message_out = "tells you how it is.\n"+s
        
        return "/me %s" % message_out
