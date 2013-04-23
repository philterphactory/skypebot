# coding=UTF-8

from string import Template
import random

import pkgutil
import commands

from commandbase import BaseCommand

class WhutCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "cmd", "whut" ]
        
    def generate( self, name ):

# hacked out until i can work out the meta-problem


        # import commands
#        a_commands = []

        ## load all commands
#        reload( commands )
#        for loader, modname, ispkg in pkgutil.iter_modules( commands.__path__, prefix="commands." ):
        

#            module = __import__( modname, fromlist="dummy" )
#            reload( module )
#            for klassname in dir( module ):
#                if "Command" in klassname and "BaseCommand" not in klassname:
                    
                    
#                    kommandklass = getattr( module, klassname )
#                    kommand = kommandklass()
#                    a_commands.append( kommand )
#        out='commands: '
#        for cmd in a_commands:
#            l=cmd.command_mappings
#            for c in l:
#                out=out+c+' '
            
#        message_out = out
#        return "/me %s" % message_out
        return "/me /me commands: aces adman tony albeit anger bile fuck art artist bacon ball bar bash benchmark birthday bullshit semiotics bye night cat pussy ceo chief boss cheese chill choon client cock coffee cmd whut anus chickentown christmas chrimble santa w3t splashy ffs goon bouncer hoyle atom atomoil kick ban evict bar loon mad doit mynew new peter pit bihr dovey german shootout sxe edge trial Waaaassssaaaap cunt doris louisa deskbeer drink elvis bored ennui eurovision ferbs sarah freud grass hai ohai hallo morning afternoon evenin ham dovehand hand hands hangover hungover henry hank hipster hat heckle help lightweight love lsp marcus kaiser Kaiser kamerad mate seriously mjays spindler spider photoshop chicken ponder povey owl fractal prezi preyi prog purps nurps purple sime quiz recap regrets myway brawl rumble botsola landlord lndlrd mullet satan dave lobster stan shardcore shardy eric silvertips batsign shoutout bigup holdtight smoke deskpizza snack weare social twitter smebs pinterest startup hoxton shoreditch stats eno brian strategy oblique tea cuppa brew tiny Copperfield McGee maagik magikk trick magic tv advice 8ball fortune twocents tip warning word vendor voodoo witch spell war bomb w3t splashy who"
        
