# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class BingoCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "bingo" ]
        self.templates = [  Template("Kelly's Eye - 1."),
                            Template("One Little Duck - 2."),
                            Template("Cup of tea - 3."),
                            Template("Knock at the door - 4."),
                            Template("Man alive - 5."),
                            Template("Tom Nix - 6."),
                            Template("God's in heaven - 7."),
                            Template("One Fat Lady - 8."),
                            Template("Doctor's orders - 9."),
                            Template("Blind 10."),
                            Template("Legs eleven."),
                            Template("Baker's dozen - 11."),
                            Template("Key of the door - 21."),
                            Template("Two little ducks - 22."),
                            Template("Duck and dive - 25."),
                            Template("You're doing fine - 29."),
                            Template("Burlington Bertie - 30."),
                            Template("Buckle my Shoe - 32."),
                            Template("Dirty knees - 33."),
                            Template("Naughty 40."),
                            Template("Time for fun - 41."),
                            Template("Down on your knees - 43."),
                            Template("Droopy drawers - 44."),
                            Template("Halfway house - 45."),
                            Template("Four and seven - 47."),
                            Template("Nick nick - 49."),
                            Template("Tweak of the thumb - 51."),
                            Template("Danny La Rue - 52."),
                            Template("Stuck in the tree - 53."),
                            Template("Snakes alive - 55."),
                            Template("Heinz varieties - 57."),
                            Template("Brighton line - 59."),
                            Template("Tickety boo - 62."),
                            Template("Tickle me - 63."),
                            Template("Clickety click - 66."),
                            Template("Your place or mine - 69."),
                            Template("Candy store - 74."),
                            Template("All the sevens - 77."),
                            Template("Heaven's gate - 78."),
                            Template("Staying alive - 85."),
                            Template("Top of the shop - 90.") ]	


    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out