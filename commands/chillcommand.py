# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ChillCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "chill" ]
        self.templates = [  Template("tells $name to chill the fuck out."),
                            Template("tells the !Kaiser to chill the fuck out."),
                            Template("can see that $name is already very chilled and tells the !Kaiser to chill the fuck out."),
                            Template("bars $name for being too punchy."),
                            Template("puts $name on the special un-chill list."),
                            Template("pours everyone a !drink, on the house.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out