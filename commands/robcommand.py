# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class RobCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "rob" ]
        self.templates = [  Template("wears too much black in Texas."),
                            Template("rolls his eyes at !satan"),
                            Template("emigrates."),
                            Template("loves him some !elvis"),
                            Template("writes it up."),
                            Template("CC licenses himself."),
                            Template("open sources himself."),
                            Template("publicly acknowledges that perl is superior to python."),
                            Template("leaves the country for !love.")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
