# coding=UTF-8

from string import Template
import random
from commandbase import BaseCommand

class DrinkCommand( BaseCommand ):

    def __init__(self):

        BaseCommand.__init__( self )
        
        self.command_mappings = [ "drink" ] 

        self.templates = [  Template("begrudgingly serves $name $drink."),
                            Template("ostentatiously prepares $name $drink and pockets the change."),
                            Template("eyeballs $name for a moment, then shoves $drink across the bar."),
                            Template("fills up $drink for $name from the drips tray."),
                            Template("waves his hands and $drink appears in front of $name in a puff of sulphurous smoke."),
                            Template("extrudes a pseudopod in the direction of $name, bearing $drink."),
                            Template("points out that $name has had enough already (drunk)"),
                            Template("does his best Tom Cruise impression and mixes $drink into a tall glass for $name."),
                            Template("stops watching the sports for a minute. Long enough to top up $drink for $name."),
                            Template("suggests that $name can go somewhere else if they want $drink. Disgusting drink."),
                            Template("longs for closing time."),
                            Template("pulls $drink from his arse for $name."),
                            Template("puts another dime in the jukebox, forgets to make $name a drink."),
                            Template("is a bit tipsy, spills a $drink all over $name's lap."),
                            Template("sieves the flies out of $drink for $name."),
                            Template("challenges $name to a shot-drinking content. First up: $drink."),
                            Template("drops everything just for $name, ungraciously prepares $drink."),
                            Template("calls the law. $name was caught doing lewd acts in the toilets."),
                            Template("shakes $drink all over $name's nice new face."),
                            Template("calmly explains to $name that $drink was always there, and vanishes.")
                            ]
        
        self.pre_modifiers = [ "half a",
                   "a stingy",
                   "a watery",
                   "a pitcher of",
                   "a cloudy",
                   "a glitchy",
                   "a splashy",
                   "a broken",
                   "a miniature",
                   "a piss-bubbling",
                   "an arse wretching",
                   "a vomit-encouraging",
                   "an imported",
                   "a back-street",
                   "a worm-filled",
                   "a mouldy",
                   "a horny",
                   "a disabled",
                   "a QR code engraved",
                   "a Jubilee-edition",
                   "a Chinese interpretation of",
                   "an over-strength",
                   "an horrific",
                   "a most erotic",
                   "a quart of",
                   "a fur-lined",
                   "a luminous",
                   "an acid-laced",
                   "the opposite of a" ]                
        
        self.drinks = [ "Beer",
            "Ale",
            "Bongwater",
            "Barleywine",
            "Bloody Mary",
            "Delirium Tremens",
            "Bitter ale",
            "Mild ale",
            "Pale ale",
            "Porter",
            "Stout",
            "Cask ale",
            "Stock ale",
            "Fruit Beer",
            "Lager beer",
            "Bock",
            "Dry beer",
            "Maerzen",
            "Pilsener",
            "Schwarzbier",
            "Sahti",
            "Small beer",
            "Wheat beer",
            "Witbier White Beer",
            "Hefeweizen",
            "Cauim",
            "Four Roses Bourbon"
            "Chicha",
            "Cider",
            "Huangjiu",
            "Icariine Liquor",
            "Kilju",
            "Kumis",
            "Lappish Hag's Love Potion",
            "Mead",
            "Palm wine",
            "Perry",
            "Plum jerkum",
            "Pulque",
            "Sake",
            "Sonti",
            "Tepache",
            "Tonto",
            "Tiswin",
            "Wine",
            "Fruit wine",
            "Table wine",
            "Sangria",
            "Champagne",
            "Port",
            "Madeira",
            "Marsala",
            "Sherry",
            "Vermouth",
            "Vinsanto",
            "Absinthe",
            "Akvavit",
            "Arak",
            "Arrack",
            "Baijiu",
            "Cachaca",
            "Gin",
            "Damson gin",
            "Sloe gin",
            "Gulu",
            "Horilka",
            "Kaoliang",
            "Maotai",
            "Mezcal",
            "Ogogoro",
            "Ouzo",
            "Palinka",
            "Pisco",
            "Rakia",
            "Slivovitz",
            "Rum",
            "hot chocolate"
            "PG Tips"
            "Soju",
            "Tequila",
            "Vodka",
            "Metaxa",
            "Whisky",
            "Bourbon",
            "Scotch",
            "Tennessee whiskey",
            "Brandy",
            "Armagnac",
            "Cognac",
            "Damassine",
            "Himbeergeist",
            "Kirsch",
            "Poire Williams",
            "Williamine",
            "Zwetschgenwasser",
            "Lambrini",
            "Paint thinner",
            "Grog",
            "Moonshine",
            "Cider",
            "Scrumpy",
            "Chartreuse",
            "Jägermeister",
            "Obstler",
            "Satan's Bier",
            "Markov Fine Lager",
            "Markov Fine Lager - Extra Splashy", 
            "Markov Fine Lager - Extra Splishy",
            "Markov Fine Lager - Extra !w3t",
            "Markov Fine Lager with a pixel twist",
            "Glitch",
            "Glitch !Bacon Flavour",
            "Glitch !Cheese And Onion Flavour",
            "Glitch !w3t",
            "Glitch !Ponder Edition",
            "Tiny",      
            "Slurp",     
            "Peppermint Schnaps",
            "Fernet Branca" ]

    def generate( self, name ):
        drink = random.choice( self.drinks )
        pre_modifier = random.choice( self.pre_modifiers )
        if(pre_modifier[-1].lower() == 'a') and (drink[:1].lower()=='a'):
            pre_modifier += "n"
        drink = "%s %s" % (pre_modifier, drink)
        template = random.choice( self.templates )
        message_out = template.substitute(name=name, drink=drink)
        return "/me %s" % message_out
        

class DeskBeerCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "deskbeer"]
        self.templates = [  Template("hurriedly brings a beer to $name's desk."),
                            Template("wonders why $name is still in the office."),
                            Template("opens a beer on the edge of the table."),                            
                            Template("spills $drink on his MacBook Air."),
                            Template("uses a post-it note as a beer mat."),
                            Template("tries to find a place to hide the empty beer bottles"),
                            Template("settles for a warm Beck's."),
                            Template("is a bit drunk off half a bottle of beer."),
                            Template("is only really looking at tumblr now."),
                            Template("has an Altoid to cover up beer breath."),
                            Template("advises $name to look for the hip flask in the desk drawer.")
                         ]
        self.morning_templates = [  Template("pours a cold $drink onto $name's cornflakes."),
                            		Template("wonders how $name made it to the office, offers them a $drink to make up for the trauma.")
                         ]
        self.drinks = [ "Beer",
            "Ale",
            "Bongwater",
            "Barleywine",
            "Bloody Mary",
            "Delirium Tremens",
            "Bitter ale",
            "Mild ale",
            "Pale ale",
            "Porter",
            "Stout",
            "Cask ale",
            "Stock ale",
            "Fruit Beer",
            "Lager beer",
            "Bock",
            "Dry beer",
            "Maerzen",
            "Pilsener",
            "Schwarzbier",
            "Sahti",
            "Small beer",
            "Wheat beer",
            "Witbier White Beer",
            "Hefeweizen",
            "Cauim",
            "Four Roses Bourbon"
            "Chicha",
            "Cider",
            "Huangjiu",
            "Icariine Liquor",
            "Kilju",
            "Kumis",
            "Lappish Hag's Love Potion",
            "Mead",
            "Palm wine",
            "Perry",
            "Plum jerkum",
            "Pulque",
            "Sake",
            "Sonti",
            "Tepache",
            "Tonto",
            "Tiswin",
            "Wine",
            "Fruit wine",
            "Table wine",
            "Sangria",
            "Champagne",
            "Port",
            "Madeira",
            "Marsala",
            "Sherry",
            "Vermouth",
            "Vinsanto",
            "Absinthe",
            "Akvavit",
            "Arak",
            "Arrack",
            "Baijiu",
            "Cachaca",
            "Gin",
            "Damson gin",
            "Sloe gin",
            "Gulu",
            "Horilka",
            "Kaoliang",
            "Maotai",
            "Mezcal",
            "Ogogoro",
            "Ouzo",
            "Palinka",
            "Pisco",
            "Rakia",
            "Slivovitz",
            "Rum",
            "hot chocolate"
            "PG Tips"
            "Soju",
            "Tequila",
            "Vodka",
            "Metaxa",
            "Whisky",
            "Bourbon",
            "Scotch",
            "Tennessee whiskey",
            "Brandy",
            "Armagnac",
            "Cognac",
            "Damassine",
            "Himbeergeist",
            "Kirsch",
            "Poire Williams",
            "Williamine",
            "Zwetschgenwasser",
            "Lambrini",
            "Paint thinner",
            "Grog",
            "Moonshine",
            "Cider",
            "Scrumpy",
            "Chartreuse",
            "Jägermeister",
            "Obstler",
            "Satan's Bier",
            "Markov Fine Lager",
            "Markov Fine Lager - Extra Splashy", 
            "Markov Fine Lager - Extra Splishy",
            "Markov Fine Lager - Extra !w3t",
            "Markov Fine Lager with a pixel twist",
            "Glitch",
            "Glitch !Bacon Flavour",
            "Glitch !Cheese And Onion Flavour",
            "Glitch !w3t",
            "Glitch !Ponder Edition",
            "Tiny",      
            "Slurp",     
            "Peppermint Schnaps",
            "Fernet Branca" ]

    def generate( self, name ):
    	hour_now = int(time.strftime("%H"))
    	if (hour_now < 12):
        	template = random.choice( self.morning_templates )
        else:
        	template = random.choice( self.templates )
        drink = random.choice( self.drinks )
        message_out = template.substitute(name=name, drink=drink)
        return "/me %s" % message_out