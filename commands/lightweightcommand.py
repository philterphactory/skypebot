# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ArtCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "lightweight" ]
        self.templates = [  Template("grabs the mop and tuts at the mess $name has made"),
                            Template("calls an ambulance for $name") ] 

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 