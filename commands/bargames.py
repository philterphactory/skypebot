# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class BargamesCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "game","bargame" ]
        self.templates = [  Template("asks $name if they's like to step up to the oche and play some darts."),
                            Template("invites $name to a game of pool. winner stays on."),
                            Template("invites $name to a cardgame, after hours."),
                            Template("sees that $name just needs treble top to win."),
                            Template("chalks his cue."),
                            Template("stacks some pound coins on the side of the pool table."),
                            Template("sits down to a game of dominoes"),
                            Template("invites $name to a game of drunk chess."),
                            Template("saunters over to the billiard table")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
