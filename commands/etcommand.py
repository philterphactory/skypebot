# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class etcCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = ["etc"]
        self.templates = [  Template("shoves the usual down the bar towards $name."),
                            Template("is getting bored by $name always ordering the same shit."),
                            Template("sees $name enter, starts doing their standard drin.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
