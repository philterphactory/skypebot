# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class MynewCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "mynew", "new" ]
        self.templates = [  Template("understands that $name's new $startup is called \"$word\".") ]
        self.startup = [ "startup",
            "thing",
            "product",
            "habit",
            "position",
            "desire",
            "beau" ]

        self.word = [ "Social Media Narcissism",
            "Guru Zentrum",
            "Corporate Density",
            "Spatial Complexity",
            "Loving Spoonful",
            "Braun Zucker",
            "Algorithmic Data Massage",
            "New Aesthetic Fashion",
            "Financial Jiu Jitsu",
            "Culture Jam",
            "Cube Farm",
            "Beanbag Office",
            "Stress Puppy",
            "Food Stamps",
            "Seagull Management",
            "Ninja Central",
            "Handsome Adult",
            "Bereaved Objects",
            "Absolute Nothingness",
            "Don\'t ruin a good story with numbers!",
            "Pipe Bomb",
            "True Say",
            "!startup",
            "Handspeed Record",
            "Stealth Made",
            "Broken Windows",
            "Me or the Chief",
            "Shitfaced & Reeling",
            "WAZZOCK, Inc.",
            "Dance Syndrome",
            "Adam Hoyle's Massive !Anus",
            "Engagement Metrics",
            "Barry",
            "Piss und Shit",
            "Creative Technologisms",
            "Dedicated Solutioneering",
            "Don\'t Call It a !startup",
            "Blended Synergy",
            "Billy Cosby Sweater Design" ]

    def generate( self, name ):
        startup = random.choice( self.startup )
        word = random.choice( self.word )
        template = random.choice( self.templates )
        message_out = template.substitute(word=word,name=name, startup=startup)
        return "/me %s" % message_out