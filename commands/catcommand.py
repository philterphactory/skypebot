# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class CatCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "cat","pussy" ]
        self.templates = [  Template("purrs."),
                            Template("licks his own genitals."),
                            Template("yowls for some food."),
                            Template("demands attention."),
                            Template("hides in a box."),
                            Template("falls asleep in the sun."),
                            Template("sheds."),
                            Template("licks the butter."),
                            Template("does something unspeakable in the litter tray."),
                            Template("has a snooze."),
                            Template("brings in an evicerated mouse."),
                            Template("pees up the wall."),
                            Template("sits on the lap of $name."),
                            Template("rubs against $name's legs."),
                            Template("eats a fly."),
                            Template("finds a sunny spot to sleep."),
                            Template("can't be bothered to wake up."),
                            Template("has horrible breath."),
                            Template("wants some tuna."),
                            Template("implacably receives the strokes of $name"),
                            Template("chases a lazer pointer")]
        
    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
