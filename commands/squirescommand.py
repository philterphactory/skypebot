# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class SquiresCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "squires","imperica" ]
        self.templates = [  
            
            Template("looks a bit like !purps"),                                                        
            Template("writes a funding application"),                                                        
            Template("blogs prodigiously"),                                                        
            Template("can't spell peroni - demands another !drink"),                                                        
            Template("remembers everyone from Big Brother"),                                                        
            Template("sells his flat in south wales"),                                                        
            Template("misspelled peroni at companies house"),                                                        
            Template("is an elusive character"),                                                        
            Template("programs in BASIC"),                                                        
            Template("puts on an event"),                                                        
            Template("interviews !eric, !povey, !nurps and !satan"),                                                        
            Template("loves his !art"),                                                        
            Template("digs out his speccy"),                                                        
            Template("demands a tip"),                                                        
            Template("publishes to the webmongs"),                                                        
            Template("is not afraid of online begging"),                                                        
            Template("kickstarts something vague"),                                                        
            Template("something something oxford"),                                                        
            Template("lives in an ivory tower"),                                                        
            Template("is not sure if it's !art or !design"),                                                        
            Template("is all about the new futures"),                                                        
            Template("loves a bit of co-development"),                                                        
            Template("speaks welsh"),                                                        
            Template("says 'boro da'"),                                                        
            Template("sings 'Mae gen i griw hyfryd o cnau coco'")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
