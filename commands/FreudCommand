# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class FreudCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "freud" ]
        self.templates = [  Template("asks $name to tell him about their mother"),
                            Template("hands $name a cigar and asks how they feel about what they are sucking on."),
                            Template("longs for a father figure.")                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out