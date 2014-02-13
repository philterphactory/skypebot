# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ProgCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "prog" ]
        self.templates = [  Template("does a 10-minute guitar solo."),
                            Template("sings something about wood nymphs."),
                            Template("grows his hair."),
                            Template("opens his third eye."),
                            Template("buys a camper van."),
                            Template("cocks his leg and twiddles around with a flute"),
                            Template("is at the controls of a MASSIVE SYNTH."),
                             ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 
