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
        
class AnusCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "anus" ]
        self.templates = [  Template("(moon)"),
                            Template("goes all yadda yadda yadda"),
                            Template("looks at a picture of !satan")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
        
class BossCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "ceo", "chief", "boss" ]
        self.templates = [  Template("thinks profit is for posers"),
                            Template("believes that it's not about the cash in the bank, it's all about the 'length of the runway'."),
                            Template("thinks this time next year, we'll be millionaires."),
                            Template("is spending money to make money."),
                            Template("is wearing a suit jacket and jeans."),
                            Template("spunked all the company's money on shiny leather upholstery."),
                            Template("has a terrific burn-rate")
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


class GoonCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "goon", "bouncer" ]
        self.templates = [  Template("leans on $name."),
                            Template("kneecaps $name."),
                            Template("asks $name to take a seat."),
                            Template("cracks his knuckles."),
                            Template("flashes a toothless grin at $name."),
                            Template("doesn't have a neck."),
                            Template("rotates his head, crunching his bones."),
                            Template("is wearing a donkey jacket."),
                            Template("tells $name to behave."),
                            Template("emails $name a toe."),
                            Template("can't be bought."),
                            Template("is selling DVD-players round the back of the pub."),
                            Template("thinks $name wants to 'ave a bit of fun."),
                            Template("posts a naked picture of $name to their family."),
                            Template("knows a thing or two about $name."),
                            Template("peels an orange, very bloody slowly."),
                            Template("bundles $name into the boot of his Vauxhall."),
                            Template("has a picture of $name's family."),
                            Template("thinks $name has a nice place here. Be a shame if anything happened to it."),
                            Template("suggests that $name should know what's good for them."),
                            Template("mutters something vaguely menacing in a gravelly voice to $name.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class LoonCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "loon", "mad" ]
        self.templates = [  Template("wears a foil !hat."),
                            Template("has mercury poisoning."),
                            Template("believes David Icke."),
                            Template("talks to himself."),
                            Template("hasn't washed for weeks."),
                            Template("doesn't trust the barge folk."),
                            Template("has all his money in carrier bags under the bed."),
                            Template("is concerned about all the lizards."),
                            Template("is carrying a copy of Catcher In The Rye."),
                            Template("cuts out bits of newspapers for his scrapbooks."),
                            Template("is still listening to !gangnam."),
                            Template("is late for a !tea party."),
                            Template("thinks $name has stolen his thoughts."),
                            Template("is called Bobbin. Are you my mother?")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

