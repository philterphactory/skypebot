# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class StartupCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "startup" ]
        self.templates = [  Template("pivots."),
                            Template("is Angel-funded by Ashton fucking Kutcher."),
                            Template("has run out of budget."),
                            Template("burns the midnight oil."),
                            Template("burns the candle from both ends."),
                            Template("asks $name for some more ramen."),
                            Template("is all hot on SoLoMo."),
                            Template("fantasizes about being featured on TechCrunch."),
                            Template("can’t seem to find any talent."),
                            Template("pitches $name while they pee."),
                            Template("is super excited about that new js framework (or was that rub?)"),
                            Template("is going to change the world with his Daily Deals site."),
                            Template("got a solid friends & family round from $name\'s Grandma."),
                            Template("doesn\'t wash the hand that shook Mike Butcher\'s.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out