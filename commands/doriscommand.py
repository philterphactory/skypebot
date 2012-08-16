# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class DorisCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "doris" ]
        self.templates = [  Template("drinks all the gin."),
                            Template("drinks !satan under the table."),
                            Template("goes for a road trip."),
                            Template("drinks !satan under the table."),
                            Template("does the deckless !dovehand.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out