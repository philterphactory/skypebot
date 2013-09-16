# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class KarmaCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "karma" ] 


        self.wisdom = [ 
            "How people treat you is their karma; how you react is yours.",
            "I believe in Karma. If the good is sown, the good is collected. When positive things are made, that returns well.",
            "A man is born alone and dies alone; and he experiences the good and bad consequences of his karma alone; and he goes alone to hell or the Supreme abode.",
            "To go from mortal to Buddha, you have to put an end to karma, nurture your awareness, and accept what life brings.",
            "Regardless of what we do, our karma has no hold on us.",
            "Life will give you whatever experience is most helpful for the evolution of your consciousness. How do you know this is the experience you need? Because this is the experience you are having at the moment.",
            "Life is painful. It has thorns, like the stem of a rose. Culture and art are the roses that bloom on the stem. The flower is yourself, your humanity. Art is the liberation of the humanity inside yourself.",
            "Leave behind the passive dreaming of a rose-tinted future. The energy of happiness exists in living today with roots sunk firmly in reality's soil.",
            "A great human revolution in just a single individual will help achieve a change in the destiny of a nation and, further, can even enable a change in the destiny of all humankind.",
            "The law is simple. Every experience is repeated or suffered till you experience it properly and fully the first time."]

        

        self.templates = [  Template("advises $name: "),
                            Template("lays it down: "),
                            Template("admonishes $name: ")
                            ]
                            
    def generate( self, name ):
        template = random.choice( self.templates )
        quote = random.choice( self.wisdom );
        message_out = template.substitute(name=name)+"\""+quote+"\"";
        return "/me %s" % message_out
