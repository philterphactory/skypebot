# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class MarcusCommand( BaseCommand ):

	def __init__(self):
		BaseCommand.__init__( self )
		self.command_mappings = [ "marcus", "kaiser", "Kaiser" ]
		self.templates = [ 	Template("tells a story."),
					Template("makes it transmedia."),
					Template("is attacked by a turkey."),
					Template("pisses about on the internet."),
					Template("ponders the tinyweb."),
					Template("thinks that the bald mullet was never a good look."),
					Template("gets a larger pair of glasses."),
					Template("puts on a wig."),
					Template("is going on a walk for Dr Peter Figge."),
					Template("fucking hates camping."),
					Template("is hanging out with Sacha."),
					Template("says poorly nothing."),
					Template("eulogises The Undertaker."),
					Template("has come down with a raging case of SMEBS."),
					Template("asks $name to do him a fucking brand onion."),
					Template("is enjoying the benefits of an excellent hangover."),
					Template("is dating Pambot."),
					Template("thinks Marcus has got a little bit carried away using his ego-command."),
					Template("giggles."),
					Template("Skypes from the pub."),
					Template("hates tellycuntery."),
					Template("gets an early night."),
					Template("is listening to self-help ebooks."),
					Template("tells !satan off for his habit."),
					Template("takes a photo of his feet by a Swiss lake."),
					Template("flirts with a marketeer."),
					Template("thinks $name is a tiny bit shit."),
					Template("engages Big Hand Mode."),
					Template("is really telling you something here. #globe_hands"),
					Template("paints his face white."),
					Template("stalks $name."),
					Template("broadcasts from the toliet."),
					Template("retires a version of himself."),
					Template("smacks a unicorn."),
					Template("flies off on a tangent."),
					Template("considers the drillability of it all."),
					Template("uses a nasty hashtag."),
					Template("makes a spelling mistake."),
					Template("says something in German."),
					Template("clones himself."),
					Template("iPod sings."),
					Template("forgets to commit the changes."),
					Template("eats some sausage."),
					Template("books a table at the Schwarzer Hahn."),
					Template("takes a photograph of !satan."),
					Template("talks for 17 minutes, poorly."),
					Template("sells $name some used web."),
					Template("charts a story."),
					Template("makes it !social"),
					Template("disappears from the bar for ages"),
					Template("falls in !love"),
					Template("forgets about the bar"),
					Template("suggests we make something"),
					Template("goes to work on his !tiny farmyard."),
					Template("doesn't come round here no more."),
					Template("ponders the notion he could be an !adman.")
					]
							
	def generate( self, name ):
		template = random.choice( self.templates )
		message_out = template.substitute(name=name)
		return "/me %s" % message_out


class SacrumCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "dovey","german" ]
        self.templates = [  Template("sends $name much warmth."),
                            Template("is European man with skills in advertising."),
                            Template("has his own pencils."),
                            Template("got in to funky advertising agency."),
                            Template("sharpen pencil and top-up mobile phone."),
                            Template("is availability on Wednesdays and CVon request."),
                            Template("applies for a job at W+K."),
                            Template("is sending out the right charges for right customer."),
                            Template("is thanking you from his bottom."),
                            Template("has brand warmness."),
                            Template("seek advices from key figures in marketing arena.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out
