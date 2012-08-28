# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class ClientCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "client" ]
        self.templates = [  Template("asks $name if they could make a microsite to go with the project."),
                            Template("requests that $name just make some !tiny changes. It won't take long."),
                            Template("has run out of budget."),
                            Template("delays decisions."),
                            Template("has partners to satisfy."),
                            Template("has not read the spec."),
                            Template("would like a BlackBerry version of the app."),
                            Template("forgets about the British bank holidays."),
                            Template("insists that the logo be bigger."),
                            Template("can't see it on their iPad."),
                            Template("is in a meeting."),
                            Template("doesn't get it."),
                            Template("has given the job to his nephew."),
                            Template("has just called to say that he has sent you an Email."),
                            Template("nods."),
                            Template("has just read an article in Fast Company and changes everything."),
                            Template("is all about low hanging fruit right now."),
                            Template("wants to go viral."),
                            Template("likes what Apple did."),
                            Template("thinks it lacks oommpph."),
                            Template("wants to win a black pencil."),
                            Template("has been playing about with Flash."),
                            Template("is still writing the briefing."),
                            Template("tells $name that his wife doesn't like the colour."),
                            Template("has a closed door policy."),
                            Template("is pitching."),
                            Template("wants to make a splash in the Russian market."),
                            Template("disagrees with the research."),
                            Template("is bored with the treatement."),
                            Template("doesn't have $name's version of PowerPoint."),
                            Template("has stakeholders to satisfy."),
                            Template("doesn’t want to boil the ocean."),
                            Template("demands actionable deliverables."),
                            Template("wonders how this will fit with corporate."),
                            Template("needs to check with legal."),
                            Template("really does not want to pay."),
                            Template("changes his mind.")
                            ]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out