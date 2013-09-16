# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class DivaCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "diva" ]

        self.templates = [  Template("flounces out."),
                            Template("promises to punch $name in the face."),
                            Template("learnt all his best moves from !purps")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

