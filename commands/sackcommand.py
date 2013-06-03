# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class SackCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "sack","fire" ]
        self.templates = [  Template("gives $name their marching orders"),
                            Template("reports $name to HR"),
                            Template("demotes $name"),
                            Template("ejects $name from the factory and burns their tools"),
                            Template("fires $name"),
                            Template("sacks $name"),
                            Template("suggests $name should seek employment elsewhere"),
                            Template("refuses to write $name a reference"),
                            Template("hands $name his P60")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
