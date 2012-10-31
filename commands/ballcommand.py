# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class BallCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "ball" ]
        self.templates = [  Template("brings a revolutionary new product to the creative play market."),
                            Template("creates a new, new, new creative play device for you and your crushingly middle class friends and family."),
                            Template("says \'This product really is a paradigm shift in play.\'"),
                            Template("says \'And this is it. We call it a ball. A fucking ball.\'"),
                            Template("moves across more than one plane - up, down, front, back, even left and right."),
                            Template("suggests you grab a ball, bugger off into the back garden and bring your play back to life.")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
