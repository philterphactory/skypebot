# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class DeskwineCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "deskwine" ]
        self.templates = [  Template("buys some cheap french shit from the corner shop."),
                            Template("strains the flies out of last night's left-over bottle."), 
                            Template("offers $name a glass of red"), 
                            Template("offers $name a glass of white"), 
                            Template("asks if $name would like red or white"), 
                            Template("breaks out the Margaux"), 
                            Template("buys something with a screw top"), 
                            Template("thinks !deskbeer would be more economical"), 
                            Template("suggests $name tries some !deskcrack instead"), 
                            Template("pours some cheap plonk into a dirty coffee mug"), 
                            Template("says you should be happy with !drink"), 
                            Template("uncorks a bottle"), 
                            Template("visits the cellar"), 
                            Template("calls $name a ponce") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
