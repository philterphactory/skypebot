# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class PurpsCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "purps","nurps","purple","sime" ]

        self.templates = [  Template("likes his whiskey."),
                            Template("takes a day trip to brighton."),
                            Template("buys a little printer."),
                            Template("blows up a red balloon."),
                            Template("buys some butter for !povey."),
                            Template("buys a ticket for the !kaiser."),
                            Template("falls off the wagon."),
                            Template("is vending."),
                            Template("can't speak to the guy next to him."),
                            Template("buys the domain name."),
                            Template("buys some headphones."),
                            Template("left the finance industry."),
                            Template("moistens a URL."),
                            Template("is still pissed off that the !client went with the shit idea."),
                            Template("is harrassing about his invoices."),
                            Template("is photographing strangers asleep."),
                            Template("dolor sit amet, consectetur adipiscing elit."),
                            Template("redacts his last statement."),
                            Template("makes peace."),
                            Template("sells on his hit."),
                            Template("has a !diva and quits the bar."),
                            Template("gives !squires a !tip"),
                            Template("looks a bit like !squires."),
                            Template("writes words for money, not !love.") ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

