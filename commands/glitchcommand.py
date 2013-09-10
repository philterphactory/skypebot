# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class GlitchCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "glitch" ]
        self.templates = [  Template("pours out a ddddddrrrrrrrdrdrdrdrrriiiiiiiinnnnnnnknknknkkkk"),
                            Template("starts editing dropbox image links"),
                            Template("puts on some autechre")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out        
