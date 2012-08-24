# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class MjaysCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "mjays", "spindler", "spider" ]
        self.templates = [  Template("is clearly the biggest !hipster."),
                            Template("looks different in Real Life."),
                            Template("pulls an internet out of his arse."),
                            Template("adds a command from the pub.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out