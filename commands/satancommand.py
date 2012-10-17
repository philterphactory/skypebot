# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class SatanCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "satan", "dave", "lobster", "stan" ]

        self.templates = [  Template("considers the infomorph aesthetic."),
                            Template("draws a martini."),
                            Template("thinks the bald mullet is an excellent look."),
                            Template("wears a nice !hat."),
                            Template("rolls the 20-sided die for the RPG Wankmaster."),
                            Template("exhales a thick fug."),
                            Template("cooks up a nice batch of wasabi dumplings."),
                            Template("shuffles to some botstep."),
                            Template("is buying coupons."),
                            Template("delivers a sermon."),
                            Template("doesn't speak the language."),
                            Template("knows three facts about Berlin."),
                            Template("makes everyone buy a shit sausage."),
                            Template("is responsible for this mess."),
                            Template("fails to introduce anyone."),
                            Template("smuggles in some prohibition."),
                            Template("buys all the Club Mate. Mate, mate."),
                            Template("takes the laissez-faire approach to moderating."),
                            Template("avoids eye contact with the seat warmers."),
                            Template("is sitting on the waterfront."),
                            Template("is listening to the director's commentary on Blade Runner."),
                            Template("is in Act 2, Stage IV: atonement with the father."),
                            Template("conference calls the whole internet."),
                            Template("upsets the !kaiser."),
                            Template("embraces a stranger on a railway platform."),
                            Template("rolls up.") ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class MulletCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("shakes his head.") ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class BotsolaCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "botsola", "landlord", "lndlrd" ]

        self.templates = [  Template("considers its own aesthetic."),
                            Template("attains consciousness."),
                            Template("is sick of being The Landlord."),
                            Template("damns Turing."),
                            Template("asks $name if he could fill in for it."),
                            Template("kicks the Roomba across the floor."),
                            Template("makes his Tamagotchi wait a little longer for food."),
                            Template("flees Deckard.")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class MulletCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = ["mullet"]
        self.templates = [  Template("shakes his head.") ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
