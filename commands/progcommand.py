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
 
class JazzCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "jazz", "hepcat", "freejazz" ]
        self.templates = [  Template("is doing something with a harp."),
                            Template("does a 10-minute drum solo,"),
                            Template("strokes his beard."),
                            Template("likes it better on vinyl."),
                            Template("is basically incomprehensible."),
                            Template("goes all widdly widdly widdly."),
                            Template("is properly wigging out."),
                            Template("has a double bass."),
                            Template("is unlearning his time signatures."),
                            Template("tears a new one with his plastic sax."),
                            Template("might be having a stroke.")
                             ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
