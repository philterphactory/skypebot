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
                            Template("hashtags an attack."),
                            Template("transmediates a ground assault."),
                            Template("assassinates $name on YouTube."),
                            Template("Instagrams the POW."),
                            Template("has got his camos on."),
                            Template("evactuates himself."),
                            Template("invites $name to the facebook event 'Pillar of Defence'."),
                            Template("violates the TOS."),
                            Template("declares war on $name."),
                            Template("storms out of the negotiations"),
                            Template("breaks the ceasefire.")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
