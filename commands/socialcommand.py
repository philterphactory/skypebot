# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class WeAreCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "weare", "social", "twitter", "smebs", "pinterest" ]
        self.platforms = [ "Facebook", "Twitter", "MySpace", "FriendsReunited", "Friendster", "Instagram", "Path", "Vine", "Flickr", "ThisIsMyJam", "HypeMachine", "RunKeeper" ]
        self.templates = [  Template("starts another $platform campaign."),
                            Template("designs another $platform app for $name."),
                            Template("bores $name shitless with excited talk about the potential for $platform apps."),
                            Template("considers making his own version of Nike+ called $name+"),
                            Template("is convinced that $platform is the new $platform2."),
                            Template("insists that $name place all their bets on the new $platform engagement strategy."),
                            Template("wonders how to seed their new viral on $platform"),
                            Template("looks for a community manager for $platform"),
                            Template("tries to convince $name that $platform is not what they want, instead it's $platform2 they're looking for.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        platform = random.choice( self.platforms )
        platform2 = random.choice(self.platforms)
        message_out = template.substitute(name=name,platform=platform, platform2=platform2)
        return "/me %s" % message_out