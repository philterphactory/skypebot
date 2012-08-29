# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class BarCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "bar" ]
        self.templates = [  Template("cheers the bar on collectively taking the piss.")
                         ] 

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 