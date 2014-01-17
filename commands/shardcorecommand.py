# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ShardcoreCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "shardcore", "shardy", "eric", "silvertips", "guyfromrealworld", "slumlord", "shard" ]
        self.templates = [  Template("paints a lovely painting of Morrissey."),
                            Template("is told to bite his tongue by $name."),
                            Template("is denied access to the United States of Botstep."),
                            Template("is disappointed by all the swearing."),
                            Template("just wants to finger paint."),
                            Template("sacks his cleaner."),
                            Template("suaves it out."),
                            Template("gets Amazulu to play in the kitchen."),
                            Template("rents to a Trustafarian."),
                            Template("has no morals."),
                            Template("builds a massive robot cat."),
                            Template("can't taste anything."),
                            Template("!heckles the other stage."),
                            Template("puts on his black !hat."),
                            Template("slinks out in the morning."),
                            Template("is wearing a waistcoat."),
                            Template("photoshops his fingernails."),
                            Template("is an artist, from Brighton."),
                            Template("misses the real world."),
                            Template("doesn't have a face."),
                            Template("gets censored by FOX."),
                            Template("draws a face on his cock-tip."),
                            Template("has declared world domination of techno sleaze has is ultimate goal."),
                            Template("makes the bar recursive."),
                            Template("recommends the algo-bar just behind the door."),
                            Template("is in love with `select by rand()`"),
                            Template("is really into algoart lately."),
                            Template("is potentially a radio man."),
                            Template("has a serious chat with the cleaning lady."),
                            Template("demands to know about the parrot.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out


class BrightonCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("lobs a hacky sack at $name."),
                            Template("makes some !art."),
                            Template("likes it better in the winter, when all the London bastards have gone home."),
                            Template("sits on the beach"),
                            Template("puts some stuff in a !tiny box in a pub."),
                            Template("sabotages the railway line to London.") ]
        self.command_mappings = [ "brighton" ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out