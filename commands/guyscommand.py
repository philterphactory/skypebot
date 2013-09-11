# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class GuysCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "guys" ]
        self.templates = [  Template("is thoroughly disappointed with the bad behaviour on portrayal here."),
                            Template("kicks everybody out."),
                            Template("wonders what he did to deserve this."),
                            Template("needs a break. This bar is fucking insane.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out        
