# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ArtistCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "twat" ]

          self.templates = [  Template("decides that $name is not a twat."),
                    Template("decides that $name is an twat."),
                    Template("decides that $name is 50% twat."),
                    Template("decides that $name is 66.6% twat.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

