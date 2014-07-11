# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class PunkCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "punk" ]
        self.templates = [  Template("sticks it to the man."),
                            Template("sticks a sefety pin through his nose."),
                            Template("gobs on $name."),
                            Template("has only one string on his guitar, doesn't give a shit."),
                            Template("laughs at a hippie."),
                            Template("is the voice of the disenranchised."),
                            Template("questions your committment to the cause."),
                            Template("plays all the wrong notes."),
                            Template("pogos."),
                            Template("thinks he's Johnny Rotten, but is actually more Sid Snot."),
                            Template("racks up the sulphate."),
                            Template("dyes his mohawk."),
                            Template("pierces something."),
                            Template("goes !sxe"),
                            Template("flirts with some dodgy imagary"),
                            Template("fights the system."),
                            Template("screams in $name's face"),
                            Template("ODs in his squat."),
                            Template("sniffs some glue."),
                            Template("paints his leather jacket."),
                            Template("dupes some demo cassettes."),
                            Template("is basically a bit middle-class."),
                            Template("plays a power chord."),
                            Template("gets hassled by the pigs."),
                            Template("gets banned everywhere."),
                            Template("swears a bit."),
                            Template("hangs out with Ronnie Biggs"),
                            Template("takes ages to lace up his docs")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
