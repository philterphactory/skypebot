# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class BergCommand( BaseCommand ):

	def __init__(self):

		BaseCommand.__init__( self )
		
		self.command_mappings = [ "berg","littleprinter" ]

		self.templates = [ 	Template("pivots, again."),
					Template("strings out 10 lines of code into a 'business model'"),
					Template("mistakenly gets into the hardware business"),
					Template("mistakenly gets into the software business"),
					
					Template("watches everyone leave"),
					Template("something something cloud something."),
					Template("something something IoT something."),
					Template("says 'but, but, Shoreditch?!'")
						 ]


	def generate( self, name ):

		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out

