# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class BrainsCommand( BaseCommand ):

    def __init__(self):
          
          BaseCommand.__init__( self )

          self.command_mappings = [ "brain" ]

          self.templates = [  Template("assembles the wise."),
                    Template("shouts the roll call."),
                    Template("orders a meeting."),
                    Template("expects answers."),
                    Template("can't be arsed to google it."),
                    Template("wants you to do the research."),
                    Template("expects a report on his desk immediately."),
                    Template("hopes !ponder has the answer."),
                    Template("gets !povey to google it."),
                    Template("is too !hungover to work it out himself."),
                    Template("has already tried Yahoo Answers."),
                    Template("plugs into the Borg mind.")]

    def generate( self, name ):
        template = random.choice( self.templates )
        message_out = template.substitute(name=name)
        return "/me %s" % message_out

