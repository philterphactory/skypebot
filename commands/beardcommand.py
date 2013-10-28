# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class BeardCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "beard" ]
        self.templates = [  Template("suggests $name grows $btype.") ]
        
    def generate( self, name ):
        beards=['a Chin curtain','a Chinstrap beard','a French cut goatee','some Friendly muttonchops','a Fu Manchu',
'a Goat patch','a Goatee','a German Goatee','a Handlebar moustache','a Horseshoe Moustache','some Mutton chops','some Sidewhiskers','a Neckbeard','a Pencil moustache','a Shenandoah','Sideburns','a Soul patch','a Toothbrush moustache','a Van Dyke beard','some bumfluff, like a Ruby developer']
        b=random.choice(beards)
        template = random.choice( self.templates )
        message_out = template.substitute(name=name,btype=b)
        return "/me %s" % message_out
