# coding=UTF-8
from string import Template
import random
import urllib2
from commandbase import BaseCommand

class StatsCommand( BaseCommand ):

     def __init__(self):
          BaseCommand.__init__( self )
          self.command_mappings = [ "stats" ]
          self.templates = [  Template("Generating $name."),
                            ]
          self.gifting_enabled = True

     def generate( self, name ):
          template = random.choice( self.templates )
          message_out = template.substitute( name=name )
          if name.endswith( (".","!","?") ) and message_out.endswith("."):
               message_out = message_out[:-1] # lose the fullstop if name is already punctuated

          words=name.split()
          url='http://ephemera.shardcore.no-ip.org/cgi-bin/getBarStats.pl?k='+words[2]
          response = urllib2.urlopen(url)
          report = response.read()


          message_out+=report
           

          return "/me %s" % message_out

     def execute( self, message ):
          body = message.Body
          bl = body.lower()

#          response = urllib2.urlopen('http://ephemera.shardcore.no-ip.org/cgi-bin/barstats.pl?keyword='+bl)

          for commandstring in self.command_mappings:
               if commandstring in bl:
                    print commandstring
                    command_index = bl.find( commandstring )
                    print command_index
                    if command_index > -1:
                         remainder = body[ command_index + len(commandstring): ]
                         remainder = remainder.lstrip()

                         to_string = "to"
                         to_index = remainder.lower().find( to_string )
                         name = None
                         if to_index > -1:
                              name = remainder[ to_index + len(to_string): ]
                              name = name.lstrip()
                              return self.generate( name )
          name = message.FromDisplayName
          return self.generate( name )               
          
