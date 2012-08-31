# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class CeoCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "ceo", "chief", "boss" ]
        self.templates = [  Template("thinks profit is for posers"),
                            Template("believes that it's not about the cash in the bank, it's all about the 'length of the runway'."),
                            Template("thinks this time next year, we'll be millionaires."),
                            Template("is spending money to make money."),
                            Template("is wearing a suit jacket and jeans."),
                            Template("spunked all the company's money on shiny leather upholstery."),
                            Template("doesn’t want to let numbers ruin a good story."),
                            Template("freaks out in front of the board"),
                            Template("fucked up the cap table."),
                            Template("demonstrates terrific customer engagement."),
                            Template("makes up a chart."),
                            Template("has a degree in creative accounting."),
                            Template("has a terrific burn-rate")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out        
