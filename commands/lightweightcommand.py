# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class LightweightCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "lightweight" ]
        self.templates = [  Template("grabs the mop and tuts at the mess $name has made"),
                            Template("calls an ambulance for $name"),
                            Template("talks conspiratorially behind $name\s back after they leave."),
                            Template("expected so much more from $name"),
                            Template("de-invites $name from the forthcoming phactory bar coke and hookers party"),
                            Template("thinks $name should learn to hold their !drink"),
                            Template("calls $name a rude name"),
                            Template("tells $name that even !purps lasted longer than this. !ffs")

 ] 

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
 
