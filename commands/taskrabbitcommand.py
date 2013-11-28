# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class TaskrabbitCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )

        self.command_mappings = [ "taskrabbit" ]

        self.templates = [  Template("gives $name $money to $task."),
                            Template("wonders what $name would need to do $task.")
                            ]
                            
        self.task = [ "fucking sort it out",
            "drop his kegs",
            "slap the shit out of AB",
            "touch it",
            "get his laundry" ]
            
        self.money = [ "a quid",
            "a handful of dog meat",
            "a pound of !bacon",
            "two !drinks",
            "a handjob" ]
                            
    def generate( self, name ):
        task = random.choice( self.task )
        money = random.choice( self.money )
        template = random.choice( self.templates )
        message_out = template.substitute(name=name money=money, task=task)
        return "/me %s" % message_out

