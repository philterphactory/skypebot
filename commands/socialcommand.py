# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class WeAreCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "weare", "social", "twitter" ]
        self.platforms = [ "Facebook", "Twitter", "MySpace", "FriendsReunited", "Friendster", "Instagram", "Path", "Vine", "Flickr", "ThisIsMyJam", "HypeMachine", "RunKeeper" ]
        self.templates = [  Template("starts another $platform campaign."),
                            Template("designs another $platform app for $name."),
                            Template("bores $name shitless with excited talk about the potential for $platform apps."),
                            Template("considers making his own version of Nike+ called $name+"),
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        platform = random.choice( self.platforms )
        message_out = template.substitute(name=name,platform=platform)
        return "/me %s" % message_out