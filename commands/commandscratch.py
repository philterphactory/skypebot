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
        
class CampusCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "campus" ]
        self.templates = [  Template("is confused by all the noise"),
                            Template("wonders where everybody has gone"),
                            Template("bans all the booze"),
                            Template("makes a bloody killing on coupons"),
                            Template("makes $name a V.I.P."),
                            Template("does an unconference."),
                            Template("stinks of dev B.O."),
                            Template("does a crane shot."),
                            Template("plays all the noises."),
                            Template("is weirded out by the robots everywhere."),
                            Template("picks up some groupies."),
                            Template("messes about with the sound levels")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
class GangnamCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "gangnam" ]
        self.templates = [  Template("(lalala)"),
                            Template("(tmi)"),
                            Template("(\o/)")
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
        

class ClientCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "client" ]
        self.templates = [  Template("asks $name if they could make a microsite to go with the project."),
                            Template("requests that $name just make some !tiny changes. It won't take long."),
                            Template("has run out of budget."),
                            Template("delays decisions."),
                            Template("has partners to satisfy."),
                            Template("has not read the spec."),
                            Template("would like a BlackBerry version of the app."),
                            Template("forgets about the British bank holidays."),
                            Template("insists that the logo be bigger."),
                            Template("can't see it on their iPad."),
                            Template("is in a meeting"),
                            Template("doesn't get it"),
                            Template("has given the job to his nephew"),
                            Template("has just called to say that he has sent you an Email"),
                            Template("nods"),
                            Template("has just read an article in Fast Company and changes everything"),
                            Template("is all about low hanging fruit right now"),
                            Template("wants to go viral"),
                            Template("likes what Apple did"),
                            Template("thinks it lacks oommpph"),
                            Template("wants to win a black pencil"),
                            Template("has been playing about with Flash"),
                            Template("is still writing the briefing"),
                            Template("tells $name that his wife doesn't like the colour"),
                            Template("has a closed door policy"),
                            Template("is pitching"),
                            Template("wants to make a splash in the Russian market"),
                            Template("disagrees with the research"),
                            Template("is bored with the treatement"),
                            Template("doesn't have $name's version of PowerPoint"),
                            Template("changes his mind.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out