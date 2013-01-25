from commands import drinkcommand
from commands import shoutoutcommand
from commands import lspcommand
from commands import commandscratch
from commands import hankcommand
from commands import regretscommand
from commands import ballcommand
from commands import helpcommand


# stats
test_command = helpcommand.HelpCommand()
print test_command.generate( "help" )

# ponder
#test_command = pondercommand.PonderCommand()
#print test_command.generate( "prehensile" )

# shoutout
#test_command = shoutoutcommand.ShoutoutCommand()
#test_message = { "Body": "#shoutout to the berlin massive" }
#print test_command.execute( test_message )
