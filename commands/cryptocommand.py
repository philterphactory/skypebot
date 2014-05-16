# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class CryptoCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "crypto", "blockchain", "bitcoin" ]
        self.templates = [  Template("poisons the blockchain."),
                            Template("fucks around with ethereum."),
                            Template("writes !art into the blockchain."),
                            Template("is all over $name coin."),
                            Template("is living in a charles stross novel."),
                            Template("likes tor."),
                            Template("demands payment in dogecoin."),
                            Template("digs the !hipster affordances of a p2p encrypted blockchain."),
                            Template("fogets his bitcoin password."),
                            Template("buys something on silk road."),
                            Template("encrypts $name forever."),
                            Template("is like upsetting the capitalist hegemony, man."),
                            Template("puts a virus in the blockchain."),
                            Template("gets !rob to explain it all.")
                            ]


    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
