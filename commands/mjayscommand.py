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
                            Template("zooms in on a Peugeot."),
                            Template("yells !drink in a stranger's face."),
                            Template("pulls an internet out of his arse."),
                            Template("is like, totally V.I.P. in your face, ja?"),
                            Template("has a nice pair of sunglasses"),
                            Template("is potentially a ladies man."),
                            Template("adds a command from the pub.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out