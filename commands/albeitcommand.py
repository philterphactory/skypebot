# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class AlbeitCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "albeit", "infomorph", "academic" ]

          self.templates = [  Template("interrogates the human infomorph aesthetic."),
                    Template("!ponders if Blade Runnered is a term"),
                    Template("hasn't thought it through"),
                    Template("starts an albeit meme."),
                    Template("goes off on one about #civicbots."),
                    Template("tweets the response."),
                    Template("asks for a definition of ethics."),
                    Template("inserts some rhetoric."),
                    Template("stares at $name"),
                    Template("engineers the obselesence of a platform."),
                    Template("!ponders the danger of the information metaphor."),
                    Template("refers to $name an academic."),
                    Template("aggregates the results."),
                    Template("spams the !hashtag with incoherent babble."),
                    Template("is a Python script."),
                    Template("goes quiet when asked to debate in the open."),
                    Template("!ponders the paradigm shift."),
                    Template("becomes friends with a self-service checkout machine."),
                    Template("doesn't trust the algorithms."),
                    Template("bigs up the Warwick massive."),
                    Template("publicly loses !sxsw on the Twitters."),
                    Template("believes the Unified Knowledge System relies heavily on the information metaphor."),
                    Template("tells $name that the Twitter bullshit filter is working."),
                    Template("visualises the intangible."),
                    Template("loses his data."),
                    Template("doesn't attend the conference."),
                    Template("is 12 years old."),
                    Template("trolls the conference panel."),
                    Template("has soulless eyes."),
                    Template("needs more long words to hammer home his point."),
                    Template("thinks bots are an example of a reductionist technocracy."),
                    Template("is NOT a bot. Really."),
                    Template("has father issues."),
                    Template("refuses to debate with $name."),
                    Template("RTs all the research."),
                    Template("needs a dictionary."),
                    Template("tries to think in real-time. Fails"),
                    Template("flies into a tepid rage. Like an entitled chinchilla."),
                    Template("quotes himself."),
                    Template("had his bot culled."),
                    Template("constantly reconfigures its agent-world boundary"),
                    Template("is not so much constructed from technology"),
                    Template("is able to be open to the essence of technology")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

