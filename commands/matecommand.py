# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class MateCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "mate" ]
        self.templates = [  Template("is all mate, mate, seriously?")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class SeriouslyCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "seriously" ]
        self.templates = [  Template("is all seriously, seriously, mate?")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out