# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
## Also: Please indent using spaces.
class ExampleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("lobs a dolphin at $name.") ]
        self.command_mappings = [ "w3t", "splashy" ]
        self.enabled = False # change to True (or just delete this line) to enable a command

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
class ChillCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "chill" ]
        self.templates = [  Template("tells $name to chill the fuck out."),
                            Template("tells the !Kaiser to chill the fuck out."),
                            Template("can see that $name is already very chilled and tells the !Kaiser to chill the fuck out."),
                            Template("bars $name for being too punchy."),
                            Template("puts $name on the special un-chill list."),
                            Template("pours everyone a !drink, on the house.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class PeterCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "peter", "pit" ]
        self.templates = [  Template("invites $name to a conference."),
                            Template("has hours of panels to fill."),
                            Template("assembles the band")                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
