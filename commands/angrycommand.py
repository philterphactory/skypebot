# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class AngryCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "anger","bile","fuck" ]
        self.templates = [  Template("punches $name."),
                            Template("pukes on $name."), 
                            Template("starts a pointless fight with $name."), 
                            Template("invites $name outside to sort this out like gentlemen."), 
                            Template("hates the very idea of $name."), 
                            Template("kicks $name's cat down the stairs."), 
                            Template("spits on $name."), 
                            Template("endoreses $name on Linked-in for being a cunt."), 
                            Template("moshes."), 
                            Template("gives $name a dead arm."), 
                            Template("calls $name a tosser"), 
                            Template("adds $name's name to a pointless internal chain of CC emails."), 
                            Template("makes $name lick his boots."), 
                            Template("breaks into $name's house and shits on the carpet."), 
                            Template("bloodies $name's nose."), 
                            Template("poisons $name's !drink."), 
                            Template("signs $name up for nasty pr0n spam."), 
                            Template("stops $name from !dovehanding by cutting their fucking mitts off"), 
                            Template("chokes $name."), 
                            Template("weeps bitter tears of rage."), 
                            Template("is revolted by $name."), 
                            Template("says $name looks like a twat in that !hat."), 
                            Template("sticks a pin in his voodoo doll of $name."),
                            Template("refuses to !chill out."),
                            Template("post some dogshit through $name's letterbox"),   
                            Template("simply says '$name, fuck you' "),
                            Template("shoots at $name"),  
                            Template("throws a !drink in $name's face") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
