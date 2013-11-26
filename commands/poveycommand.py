# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class PoveyCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "povey", "owl" ]
        self.templates = [  Template("thinks $name completes him."),
                            Template("nurtures a hangover."),
                            Template("organises a conference"),
                            Template("makes some badges"),
                            Template("puts Side B on."),
                            Template("could go for a nap quite happily."),
                            Template("wangs all his money on Drawn & Quarterly."),
                            Template("writes an erotic ebook."),
                            Template("congratulates $name."),
                            Template("makes a shit pun."),
                            Template("as uttered forth in the public works of Puncher and Wattmann of a personal God quaquaquaqua with white beard."),
                            Template("corrects !marcus' spelling."),
                            Template("instagrams the cat."),
                            Template("forgot to add a mapping."),
                            Template("automagically grows a beard"),
                            Template("buggers off to Denmark for a bit."),
                            Template("nips out the back to catch up with the wrestling"),
                            Template("was on the best seat in the bus this morning"),
                            Template("asks if people do karaoke in Sheffield"),
                            Template("skips three slides because he can't be bothered"),
                            Template("doesn't want to do it anymore"),
                            Template("doesn't like the currywurst"),
                            Template("moans about the coupons"),
                            Template("snores like a bastard"),
                            Template("considers the !ball"),
                            Template("pukes on a cunt"),
                            Template("won't swear at the BBC"),
                            Template("does a !diva right in the middle of something"),
                            Template("doesn't remember the film being this long"),
                            Template("is annoyed by the quality of sound"),                            
                            Template("makes a dry northern comment"),
                            Template("goes for a long bike ride with just his thoughts."),
                            Template("is half the man he used to be."),
                            Template("hawks for moo."),
                            Template("doesn't like London."),
                            Template("instagrams his rhubarb creme brulee"),
                            Template("fucks off and buys some obscure 7 inches."),                                                        
                            Template("steals some !cheese from a baby"),                                                        
                            Template("calls $name a divvy")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
