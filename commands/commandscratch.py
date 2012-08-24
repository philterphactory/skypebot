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
        self.command_mappings = [ "peter", "pit", "bihr" ]
        self.templates = [  Template("invites $name to a conference."),
                            Template("has hours of panels to fill."),
                            Template("assembles the band"),
                            Template("gets the bar into SXSW."),
                            Template("fires up his !prezi"),
                            Template("goes solo")                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class FreudCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "freud" ]
        self.templates = [  Template("asks $name to tell him about their mother"),
                            Template("hands $name a cigar and asks how they feel about what they are sucking on."),
                            Template("longs for a father figure.")                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
class PhotoshopCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "photoshop", "chicken" ]
        self.templates = [  Template("thinks the photoshopped cops are photoshopped keen."),
                            Template("is keen to photoshopped keep it photoshopped clean."),
                            Template("feels that the photoshopped chief's a photoshopped swine."),
                            Template("wonders who photoshopped draws a photoshopped line."),
                            Template("points at photoshopped fun and photoshopped games."),
                            Template("dislikes the photoshopped kids he photoshopped blames."),
                            Template("is nowhere to be photoshopped found."),
                            Template("is anywhere in photoshopped town."),
                            Template("thinks the photoshopped scene is photoshopped sad."),
                            Template("thinks the photoshopped news is photoshopped bad."),
                            Template("thinks the photoshopped weed is photoshopped turf."),
                            Template("thinks the photoshopped speed is photoshopped surf."),
                            Template("thinks the photoshopped folks are photoshopped daft."),
                            Template("says don't make me photoshopped laugh."),
                            Template("it photoshopped hurts to look around."),
                            Template("is everywhere in photoshopped town."),
                            Template("is annoyed that the photoshopped train is photoshopped late."),
                            Template("remarks that you photoshopped wait you photoshopped wait."),
                            Template("is photoshopped lost and photoshopped found."),
                            Template("is stuck in photoshopped photoshop town."),
                            Template("looks out, the photoshopped view is photoshopped vile."),
                            Template("can see for photoshopped miles and photoshopped miles."),
                            Template("hears the photoshopped babies photoshopped cry."),
                            Template("weeps as the photoshopped flowers photoshopped die."),
                            Template("wretches as the photoshopped food is photoshopped muck."),
                            Template("smells the photoshopped drains are photoshopped fucked."),
                            Template("thinks the bar colour scheme is photoshopped brown."),
                            Template("feels the photoshopped pubs are photoshopped dull."),
                            Template("knows the photoshopped clubs are photoshopped full."),
                            Template("has books of photoshopped girls and photoshopped guys."),
                            Template("has photoshopped murder in his eyes."),
                            Template("knows a photoshopped bloke is photoshopped stabbed."),
                            Template("is waiting for a photoshopped cab."),
                            Template("photoshopped stays at photoshopped home."),
                            Template("can hear the photoshopped neighbours photoshopped moan."),
                            Template("wants you to keep the photoshopped racket down."),
                            Template("this is photoshopped photoshop town."),
                            Template("denies that the photoshopped pies are photoshopped old."),
                            Template("pretends that the photoshopped chips are photoshopped cold."),
                            Template("concedes that the photoshopped beer is photoshopped flat."),
                            Template("admits that the photoshopped flats have photoshopped rats."),
                            Template("knows the photoshopped clocks are photoshopped wrong."),
                            Template("feels the photoshopped days are photoshopped long."),
                            Template("accepts that it photoshopped gets you photoshopped down."),
                            Template("evidently photoshop town."),
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

