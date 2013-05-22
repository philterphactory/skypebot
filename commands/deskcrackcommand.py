# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class DeskcrackCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "deskcrack","deskdrugs","desksmack" ]
        self.templates = [  Template("passes the pipe to $name."),
                            Template("asks if $name would like a nice bit of smack instead."), 
                            Template("finds this crack a bit moreish."), 
                            Template("serves up some lovely crack."), 
                            Template("asks if $name would like some !deskbeer to go with his crack."), 
                            Template("racks up a bump for $name."), 
                            Template("suggests 'alternative methods' to pay for $name to pay for their habit."), 
                            Template("makes $name suck his dick for the hit."), 
                            Template("is all out of crack."), 
                            Template("is all amped up."), 
                            Template("melts the rocks."), 
                            Template("sells $name something white and rocky."), 
                            Template("cleans the pipe."), 
                            Template("gives $name the baggie.") ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
