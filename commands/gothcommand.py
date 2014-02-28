# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class GothCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "goth" ]
        self.templates = [  Template("paints it black"),
                            Template("backcombs his hair"),
                            Template("listens to the sisters"),
                            Template("basks in the !ennui"),
                            Template("calls $name a goth"),
                            Template("breaks up all the black with some paisley"),
                            Template("remembers the 80s"),
                            Template("releases the bats"),
                            Template("smells of patchouli"),
                            Template("hangs out in camden"),
                            Template("puts on more eyeliner"),
                            Template("does a funny backwards and forewards dance"),
                            Template("prefers the early stuff")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
