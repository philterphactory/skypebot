# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class FerbsCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "ferbs", "sarah" ]
        self.templates = [  Template("moves to Berlin."),
                            Template("instagrams a shoe.")
                        ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out