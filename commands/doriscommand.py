# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class DorisCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "doris", "louisa" ]
        self.templates = [  Template("drinks all the gin."),
                            Template("drinks !satan under the table."),
                            Template("goes for a road trip."),
                            Template("does the deckless !dovehand."),
                            Template("is shocked that $name unironically called himself a Futurist."),
                            Template("likes guitars"),
                            Template("is a secret goth"),
                            Template("was born a poor black boy in Mississipi."),
                            Template("starts a conference with !mjays"),
                            Template("enjoys some quality time with mother."),
                            Template("demonstrates the Heinrich manouver."),
                            Template("is in two places at once."),
                            Template("orders a killing."),
                            Template("kickstarters a kneecapping."),
                            Template("is all trended out."),
                            Template("doesn\'t make it ten points if he doesn\'t see ten points."),
                            Template("needs another fucking !drink."),
                            Template("invokes the no-dying clause."),
                            Template("writes some words."),
                            Template("reminds you of the Trojan Unicorn."),
                            Template("makes up a new term."),
                            Template("goes to the !tiny wooden pub"),
                            Template("gets everybody drunk."),
                            Template("hasn't had enough sleep."),
                            Template("is best mates with Oscar"),
                            Template("knows everyone."),
                            Template("likes the antlers.")
                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
