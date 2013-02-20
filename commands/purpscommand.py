# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class PurpsCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "purps","nuprs","purple","sime" ]

        self.templates = [  Template("likes his whiskey"),
                            Template("takes a day trip to brighton"),
                            Template("buys a little printer"),
                            Template("buys some butter for !povey"),
                            Template("buys a ticket for the !kaiser"),
                            Template("falls off the wagon"),
                            Template("writes words for money, not !love") ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

