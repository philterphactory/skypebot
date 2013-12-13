# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class RegretsCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "redacted","sekrit" ] 


        self.templates = [  Template("doesn't want anyone to know about his !deskcrack habit"),
                            Template("calls someone a !cunt then tries to hide it"),
                            Template("is funny for about a minute"),
                            Template("is covering up something")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute( name=name )
        return "/me %s" % message_out
