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
        
class TrialCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "trial" ]
        self.templates = [  Template("asks $name to leave, never to return."),
                            Template("thinks that it's OK for $name to stay a little while longer."),
                            Template("doesn't like Kafka."),
                            Template("gets the bouncers onto $name."),
                            Template("calls his Mafia mates."),
                            Template("has rigged the jury against $name."),
                            Template("makes $name a straw man."),
                            Template("is wearing a wig."),
                            Template("dozed off."),
                            Template("bonks $name on the head with his gavel."),
                            Template("thinks Facebook is a more suitable environ for $name."),
                            Template("asks $name to bugger off to LambdaMOO."),
                            Template("is involved in a bit of extraordinary rendition of $name."),
                            Template("invades the Ecuadorian embassy to extradite $name."),
                            Template("gives $name a perminent Phactory Bar green card.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

                
class MakeItSoCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "doit" ]
        self.templates = [  Template("shouts at $name: \"Make it so!\""),
                            Template("wonders why $name hasn't made that thing he's babbling on about yet.")
                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out     
        
        
class ChickenTownCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "chickentown" ]
        self.templates = [  Template("says the fucking beer is fucking fucked"),
                            Template("knows the fucking crisps are fucking old"),
                            Template("wants the fucking punters off his fucking back"),
                            Template("smells the fucking dope in the fucking bogs"),
                            Template("pours a fucking !drink for the fucking lads"),                                
                            Template("mops the fucking floor with a fucking mop"),
                            Template("cleans the fucking glasses with some fucking water"),
                            Template("flicks some fucking peanuts in $name’s fucking glass"),
                            Template("plays some fucking darts with the fucking some fucking darts"),
                            Template("serves a fucking !snack to the fucking law")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out 
        
        
        
class ShootoutCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "shootout" ]
        self.templates = [  Template("does gun fingers at $name."),
                            Template("makes a machine gun noise with his mouth."),
                            Template("turns around in slow motion."),
                            Template("reloads."),
                            Template("blows the smoke away from his invisible barrel."),
                            Template("spins his pretend revolver."),
                            Template("adjusts his ten-gallon hat."),
                            Template("holsters his pistol.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class AnusCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "anus" ]
        self.templates = [  Template("(mooning)"),
                            Template("goes all yadda yadda yadda"),
                            Template("looks at a picture of !satan")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
        
        
class HoyleCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "hoyle", "atom", "atomoil" ]
        self.templates = [  Template("gets a bit ranty."),
                            Template("does a !satan on !satan."),
                            Template("causes trouble."),
                            Template("twiddles knobs."),
                            Template("throws a pot."),
                            Template("makes the !client wait."),
                            Template("releases the stick insects.")
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

    
class ChristmasCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "christmas", "chrimble", "santa" ]
        self.templates = [  Template("kisses $name under the mistletoe."),
                            Template("has had too much eggnog."),
                            Template("asks if $name has kept the receipt."),
                            Template("likes a bit of the dark meat."),
                            Template("is soaked in brandy."),
                            Template("sets fire to the decorative wreath."),
                            Template("puts $name on top of the tree."),
                            Template("gets $name a book token."),
                            Template("eats all the Roses."),
                            Template("has a lame party-popper."),
                            Template("asks $name to carve a big of leg and breast.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out            


class FFSCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "ffs" ]
        self.templates = [  Template("for fucks sake, $name")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "%s" % message_out  


class KickCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "kick", "ban", "evict", "bar" ]
        self.templates = [  Template("warns $name about their behaviour."),
                            Template("points at the rules on the board. Tuts at $name."),
                            Template("reminds $name of the Bar Rules."),
                            Template("tells $name that they're on their final warning."),
                            Template("puts $name in the bins"),
                            Template("frogmarches $name off the premises."),
                            Template("shakes his head at $name.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

        
class WaaaassssaaaapCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "Waaaassssaaaap" ]
        self.templates = [  Template("nods at $name."),
                            Template("replies to $name, waaaaaaaaaassssaaaaaaaaaaapp!"),
                            Template("asks $name what they're upto."),
                            Template("is just having a Bud."),
                            Template("nods. True, true.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

class HeadDeskCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "headdesk" ]
        self.templates = [  Template("watches $name smash his head into the bar counter"),
                            Template("tries to stop $name from smashing through the cardboard wall with their head."),
                            Template("smashes $name's head into the bar counter"),
                            Template("watches $name walk by with a blood-gushing face"),
                            Template("thinks $name must have a wooden head"),
                            Template("facepalms. But it doesn't do $name's stupidity justice."),
                            Template("wonder's how $name made it this far."),
                            Template("hopes $name's table is strong enough.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out


class OdysseyCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "odyssey", "2001", "HAL" ]
        self.templates = [  Template("is afraid he can't let $name do that."),
                            Template("closes the pod-bay doors"),
                            Template("can read lips"),
                            Template("says \'my God, it\'s full of stars\'"),
                            Template("hangs out in the space station for a bit"),
                            Template("finds a monolith"),
                            Template("turns into a giant space baby"),
                            Template("insists on a surprising cameo by Leonard Rossiter"),
                            Template("says \'I know that you and $name were planning to disconnect me, and I\'m afraid that\'s something I cannot allow to happen.\'"),
                            Template("sings Daisy Daisy")
                            
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out     
 
class ApplauseCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.templates = [  Template("puts his hands together for $name."),
                            Template("stares $name dead in the eye and claps. Very. Fucking. Slowly."),
                            Template("pricks up his ears as a light round of applause patters around the bar for $name, like in cricket."),
                            Template("leads a Mexican wave for $name."),
                            Template("chucks peanuts at $name from the cheap seats.")]
        self.command_mappings = [ "applause", "applaud", "clap", "golfclap" ]
        self.enabled = True # change to True (or just delete this line) to enable a command

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
