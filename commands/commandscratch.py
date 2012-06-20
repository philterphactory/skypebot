# coding=UTF-8
from string import Template
import random
import commandbase

## Copypaste this example command to create new scratch commands
## Leave this one alone so new commands can be made from it.
class ExampleCommand( commandbase.BaseCommand ):

	def __init__(self):
		self.templates = [ 	Template("lobs a dolphin at $name.") ]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
		

class KnockKnockCommand( commandbase.BaseCommand ):

	def __init__(self):
		self.templates = [ 	Template("asks who's there.") ]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out
		
		
class AdmanCommand( commandbase.BaseCommand ):

	def __init__(self):
		self.templates = [ 	Template("does a brand onion for $name."),
					Template("leverages key influencers."),
					Template("makes it count."),
					Template("is in Cannes."),
					Template("delivers an insight to $name."),
					Template("is making a deck."),
					Template("is a T-shaped person."),
					Template("strategises."),
					Template("thinks this is the year of the mobile."),
					Template("considers what $name's metrics are."),
					Template("nicks an idea off of Youtube."),
					Template("organises a flashmob."),
					Template("instagrams a cup of coffee."),
					Template("pitches a pinterest strategy to $name."),
					Template("dabbles with Flash."),
					Template("makes a mood film."),
					Template("says he's going to Cannes."),
					Template("is on a conference call."),
					Template("makes the logo bigger."),
					Template("astroturfs."),
					Template("gives $name a plastic product."),
					Template("thinks he's Donald Fucking Draper."),
					Template("bitches about spec work."),
					Template("adds QR codes."),
					Template("fucks about with a pencil.")]

	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out

