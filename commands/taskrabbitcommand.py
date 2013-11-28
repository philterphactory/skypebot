# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class TaskrabbitCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "taskrabbit" ]

        self.templates = [  Template("!povey made me do it"),
                            Template("something task something rabbit")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

