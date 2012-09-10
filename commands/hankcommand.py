# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class HankCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "henry", "hank", "hipster" ]

        self.templates = [  Template("oils his fixie"),
                            Template("gets nominated for a BAFTA"),
                            Template("posts a photo on his tumblr"),
                            Template("makes an app for Bjork"),
                            Template("gets lost in a Git-hole"),
                            Template("goes a bit Nathan Barley"),
                            Template("hacks a teddy bear"),
                            Template("grows the biggest beard"),
                            Template("fixes Landy."),
                            Template("is on the spectrum."),
                            Template("eats a microphone."),
                            Template("maintains the !Landlord."),
                            Template("gets lost on public transport."),
                            Template("is disappointed in his macchiato."),
                            Template("is round the corner, practicing !dovehands."),
                            Template("leaves a trail of purple in his wake."),
                            Template("eviscerates Ruxpin."),
                            Template("needs some Vitamin D."),
                            Template("has some massive hipster affordances."),
                            Template("is on-site today."),
                            Template("considers rehousing the Landlord."),
                            Template("is in the Lake District."),
                            Template("makes more work for himself."),
                            Template("puts on his leather apron."),
                            Template("pretends to be his dad"),
                            Template("gouges himself with a post-commit hook"),
                            Template("misses his flight."),
                            Template("wears some skinny jeans") ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

