# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class SpookCommand( BaseCommand ):

	def __init__(self):

		BaseCommand.__init__( self )
		
		self.command_mappings = [ "spook","prism","nsa","skype" ]

		self.templates = [ 	Template("reads $name's email"),
					Template("runs a search on $name and finds $thing"),
					Template("checks PRISM for $thing"),
					Template("tells Obama all about $name's $thing"),
					Template("has got his eye on $name, he knows all about their $thing"),
					Template("denies anyone has a backdoor into his $thing") ]

		self.pre_modifiers = [ "suspicious",
				   "dodgy",
				   "suspect",
				   "incriminating",
				   "unusual activity in their"
				   ]				

		self.things = [ "emails",
			"!tinyweb activity",
			"SMS messages",
			"YouTube history",
			"Porn preferences",
			"!socialnetwork",
			"browsing habits",
			"bank transactions",
			"encrypted packets",
			"foursquare checkins",
			"LinkedIn endorsements",
			"!drinking habits"]

	def generate( self, name ):
		thing = random.choice( self.things )
		pre_modifier = random.choice( self.pre_modifiers )
		thing = "%s %s" % (pre_modifier, thing)
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, thing=thing)
		return "/me %s" % message_out
