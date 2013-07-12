# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class TransmediaCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "transmedia" ]

        self.templates = [  
            Template("spans all the channels."),
            Template("does something disruptive."),
            Template("adds an app."),
            Template("fakes the stats."),
            Template("reduces the digital friction."),
            Template("engages with all the channels, yeah?"),
            Template("does some 360 thinking."),
            Template("talks bollocks, !dovehands like a pro."),
            Template("ticks off all the demographics."),
            Template("creates a complex cross-platform narrative."),
            Template("mindmaps the future."),
            Template("makes something for the kids."),
            Template("goes viral on google+."),
            Template("storyboards."),
            Template("has read a book about semiotics."),
            Template("hires the !kaiser for a storytelling workshop."),
            Template("considers the brand onion."),
            Template("astroturfs a nationwide ARG."),
            Template("gets a wiki."),
            Template("wonders if this would work better as a BlackBerry app."),
            Template("votes up $name\'s UGC."),
            Template("explains that it isn\'t just branded content. Jeez louise."),
            Template("makes a CYOA YouTube campaign."),
            Template("can\'t quite picture the dramatic pay-off moment yet."),
            Template("sticks a QR code on some OOH ads."),
            Template("walks for Dr. Peter Figge."),
            Template("does something with a vending machine."), 
            Template("relates it all back to behavioural economics and herd thinking.")
            
            ]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
