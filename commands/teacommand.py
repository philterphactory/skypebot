# coding=UTF-8

from string import Template
import random
import time
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
			
		self.morning_teas = [ "Assam",
						"Pu-erh",
						"Builders" ]
		
		self.afternoon_teas = [ "Darjeeling First Flush",
								"Lapsang Souchong",
								"Dark Roasted Oolong",
								"Nilgiri",
								"Matcha" ]
		
		self.evening_teas = [ "Camomile tea",
							  "Peppermint infusion",
							  "Silver Needle",
							  "White Peony",
							  "Rooibos" ]
		
		self.night_teas = [ "Talisker",
							"Laphroaig" ]
			

	def generate( self, name ):
		hour_now = int(time.strftime("%H"))
		if hour_now > 19:
			tea = random.choice( self.evening_teas )
		elif hour_now > 14:
			tea = random.choice( self.afternoon_teas )
		elif hour_now > 5:
			tea = random.choice( self.morning_teas )
		else:
			tea = random.choice( self.night_teas )
		pre_modifier = random.choice( self.pre_modifiers )
		tea = "%s %s" % (pre_modifier, tea)
		template = random.choice( self.templates )
		message_out = template.substitute(name=name, tea=tea)
		return "/me %s" % message_out

