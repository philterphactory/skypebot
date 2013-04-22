# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class TeaCommand( BaseCommand ):

	def __init__(self):

		BaseCommand.__init__( self )
		
		self.command_mappings = [ "tea", "cuppa", "brew" ]

		self.templates = [ 	Template("pours $name $tea."),
							Template("stares glassy eyed at $name, then slides $tea across the bar."),
							Template("plays mother to $name, pours $tea."),
							Template("washes the leaves patiently, serves $name $tea."),
							Template("gets confused, pours $tea all over his knackers."),
							Template("looks longingly at the optics, sighs and hands $name $tea")]

		self.pre_modifiers = [ "a massive mug of",
				   "some stewed",
				   "a fine blend of",
				   "a freshly brewed",
				   "a tiny overpriced sample of SFTGFOP",
				   "a perfectly prepared cup of",
				   "a teapot full of"]				

		self.teas = [ "Assam",
			"Darjeeling First Flush",
			"Builders",
			"Earl Grey",
			"single estate Ceylon",
			"100 year old handrolled Oolong",
			"Lapsang Souchong",
			"Matcha"]
		self.times = ["",
					"" ]

	def generate( self, name ):
		tea = random.choice( self.teas )
		pre_modifier = random.choice( self.pre_modifiers )
		hour_now = time.strftime("%H")
		tea = "%s %s %s" % (pre_modifier, tea, hour_now)
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, tea=tea)
		return "/me %s" % message_out

