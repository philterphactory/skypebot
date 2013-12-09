# coding=UTF-8

from string import Template
import random
import time
from commandbase import BaseCommand

class SocksCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "socks" ] 

        self.templates = [  Template("pulls on a pair of $socks socks."),
                            Template("suggests $name should try some $socks socks."),
                            Template("pulls up his trousers revealing $socks socks.")
                            ]

        self.colours = ["red",
                        "green",
                        "blue",
                        "glitchy",
                        "vomit coloured",
                        "sparkly",
                        "day-glo",
                        "black",
                        "grey",
                        "orange",
                        "lemon coloured",
                        "threadbare",
                        "poorly darned"
                        ]
        
        self.styles = [
            "argyle",
            "thermal",
            "school",
            "!christmas",
            "toe",
            "work",
            "athletic",
            "heirloom",
            "artisan",
            "heavy duty",
            "football",
            "tennis",
            "snooker",
            "itchy",
            "bobby",
            "slouch",
            "knee high",
            "fuzzy",
            "cotton",
            "woolen",
            "tweed",
            "!povey"

            ]
    def generate( self, name ):
        style = random.choice( self.styles )
        colour= random.choice( self.colours )
        socks = "%s %s" % (colour, style)
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, socks=socks)
        return "/me %s" % message_out
