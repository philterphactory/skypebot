# coding=UTF-8
from string import Template
import random
from commandbase import BaseCommand

class EmoteCommand( BaseCommand ):

    def __init__(self):
        BaseCommand.__init__( self )
        self.command_mappings = [ "emote"]

        self.smilies = [ ':)',':(',':d','(cool)',':O',';)',
                         ';(','(:|',':|',':*',':P',':$',
                         ':^','|-)','|-(','(inlove)',']:)','(yn)',
                         '(blush)','|=)','(talk)','x(','(party)',':s',
                         '(hi)',':=x','(call)','(punch)'
                         '(yawn)','(puke)','(doh)','(angry)','(wasntme)','(party)',
                         '(worry)','(mm)','(nerd)','(:x)','(wave)','(facepalm)',
                         '(devil)','(angel)','(envy)','(wait)','(Hug)','(makeup)',
                         '(chuckle)','(clap)','(think)','(bow)','(rofl)','(whew)',
                         '(happy)','(smirk)','(nod)','(shake)','(waiting)','(emo)',
                         '(facepalm)','(fingerscrossed)','(waiting)','(lalala)',
                         '(highfive)','(wtf)','(finger)','(fubar)','(headbang)',
                         '(drunk)','(rock)','(punch)','(call)','(oliver)','(smoke)','(swear)','(tmi)']

        self.other = ['(tumbleweed)','(wfh)','(mooning)','(poolparty)','(hollest)','(soccer)',
                      '(toivo)','(zilmer)','(bug)','(clock)',
                      '(y)','(n)','(handshake)','(h)','(u)','(e)','(f)','(rain)','(sun)',
                      '(o)','(music)','(film)','(mp)','(coffee)','(pizza)','(cash)','(flex)',
                      '(cake)','(beer)','(d)','(ninja)','(dance)','(*)','(nerd)']


    def generate( self, name ):

        n=random.randrange(10)+3

        s="emotes "
        for e in range(0,n):
            i=random.choice(self.other)
            s=s+' '+i

        s=s+' and adds '+random.choice(self.smilies)+' for emphasis'
        
        return "/me %s" % s
