# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class TumbleweedCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "quiet","tumbleweed" ]
        self.templates = [  Template("watches a tumbleweed roll past."),
                            Template("polishes the glasses."),
                            Template("remembers when this place was rocking."),
                            Template("wonders where everyone is."),
                            Template("thinks he hasn't seen !satan for ages."),
                            Template("weeps quietly to himself.")
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

class KameradCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "kamerad" ]
        self.templates = [  Template("is all seriously, seriously, kamerad?")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
