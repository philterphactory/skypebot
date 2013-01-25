from commands import drinkcommand
from commands import shoutoutcommand
from commands import lspcommand
from commands import commandscratch
from commands import hankcommand
from commands import regretscommand
from commands import ballcommand
from commands import statscommand


# stats
test_command = statscommand.StatsCommand()
print test_command.generate( "stats povery" )

# ponder
#test_command = pondercommand.PonderCommand()
#print test_command.generate( "prehensile" )

# shoutout
#test_command = shoutoutcommand.ShoutoutCommand()
#test_message = { "Body": "#shoutout to the berlin massive" }
#print test_command.execute( test_message )
