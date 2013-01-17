# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class HamCommand( BaseCommand ):

    def __init__(self):
        
        BaseCommand.__init__( self )

        self.command_mappings = [ "ham" ]

        self.templates = [  Template("excitedly serves $name a few slices of $ham."),
                            Template("wangs a load of $ham on a plate for $name."),
                            Template("neatly chops some $ham for $name."),
                            Template("brushes the fur off the $ham for $name."),
                            Template("lovingly strokes $ham before sexily laying it across a mustard laden slice of bread for $name.") ]
        
        self.ham = [ "ham" ]

    def generate( self, name ):
        ham = random.choice( self.ham )
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, ham=ham)
        return "/me %s" % message_out
