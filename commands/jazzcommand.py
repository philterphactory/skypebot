# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class JazzCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "jazz", "scat" ]
        self.templates = [  Template("plays open music for open minds, man."),
                            Template("is higher than philosophy."),
                            Template("doesn't play what's there. $name plays what's not there."),
                            Template("does not fear mistakes."),
                            Template("plays it, but will tell you what it is later."),
                            Template("is the vernacular of the human soul."),
                            Template("thinks that if you have to ask what something is, you'll never know."),
                            Template("plays all the wrong notes."),
                            Template("solos for hours."),
                            Template("thinks he's Miles Davis, but is actually more Windsor Davis"),
                            Template("bores everyone."),
                            Template("plays something in 5/4 for the hell of it."),
                            Template("thinks brass instruments are acceptable."),
                            Template("strokes his !beard"),
                            Template("is a little bit behind the beat"),
                            Template("fucks around for a bit, and calls it !jazz"),
                            Template("improvises with $name.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
