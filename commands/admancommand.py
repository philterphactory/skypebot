# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class AdmanCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "adman", "tony" ]

          self.templates = [  Template("does a brand onion for $name."),
                    Template("leverages key influencers."),
                    Template("makes it count."),
                    Template("is in Cannes."),
                    Template("delivers an insight to $name."),
                    Template("is making a deck."),
                    Template("is a T-shaped person."),
                    Template("strategises."),
                    Template("puts a hashtag on the telly."),
                    Template("tells his mum he works in retail."),
                    Template("holds a focus group."),
                    Template("is wearing an urban tactical assault jacket."),
                    Template("is on a military-style bicycle."),
                    Template("is briefing at 1100h."),
                    Template("is totally slammed with meetings all day."),
                    Template("is the first in the office and the last to leave."),
                    Template("is on the line to the Amsterdam office."),
                    Template("thinks this is the year of the mobile."),
                    Template("considers what $name's metrics are."),
                    Template("wonders how the KPIs are performing."),
                    Template("call the intern over."),
                    Template("hovers behind $name’s shoulder."),
                    Template("needs more abbreviations."),
                    Template("concepts the strategy for a pitch on the brief."),
                    Template("buys new thick-rimmed glasses."),
                    Template("considers what $name's metrics are."),
                    Template("nicks an idea off of Youtube."),
                    Template("organises a flashmob."),
                    Template("instagrams a cup of coffee."),
                    Template("pitches a pinterest strategy to $name."),
                    Template("dabbles with Flash."),
                    Template("makes a mood film."),
                    Template("loves OK Go."),
                    Template("is waiting for a connecting flight."),
                    Template("is handling Slough."),
                    Template("is in Portland."),
                    Template("is at Nike Town."),
                    Template("wangs on about SoLoMoSto."),
                    Template("has seen the research."),
                    Template("sticks Google Maps into everything."),
                    Template("is double-tapping the future."),
                    Template("says he's going to Cannes."),
                    Template("is on a conference call."),
                    Template("makes the logo bigger."),
                    Template("astroturfs."),
                    Template("gives $name a plastic product."),
                    Template("thinks he's Donald Fucking Draper."),
                    Template("bitches about spec work."),
                    Template("adds QR codes."),
                    Template("fucks about with a pencil."),
                    Template("wonders whether he is an #artist"),
                    Template("must know a user's 'level'")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

