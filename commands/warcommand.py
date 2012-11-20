# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class WarCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "war","bomb" ]
        self.templates = [  Template("sends the drones in."),
                            Template("promotes his new war via social media."),
                            Template("bombs the fuck out of $name"),
                            Template("launches a missile strike."),
                            Template("joins the resistance."),
                            Template("goes underground."),
                            Template("declares war on $name."),
                            Template("storms out of the negotiations"),
                            Template("breaks the ceasefire.")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
