# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class EnnuiCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "bored","ennui" ]
        self.templates = [  Template("draws the curtains and returns to bed."),
                            Template("wonders why $name bothers."),
                            Template("starts to read a book, puts it away after the second page."),
                            Template("visits the same website for the 15th time for no particular reason."),
                            Template("idly switches the telly on and off."),
                            Template("get's lost looking at the wall paper."),
                            Template("despairs of it all."),
                            Template("contemplates mortality."),
                            Template("gazes into the distance."),
                            Template("quotes Wilde: \"I am tired of myself to-night. I should like to be somebody else.\""),
                            Template("retreats from the world."),
                            Template("goes for a long walk alone.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
