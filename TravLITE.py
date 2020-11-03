#
# The beginnings of a LITE chargen app for Traveller NPCs.
#
# Written for Python 2.5.4.
#
# bottle will be needed in the future at some point in this code.
#
#
# The Traveller game in all forms is owned by Far Future Enterprises.
# Copyright 1977 - 2020 Far Future Enterprises.
# Traveller is a registered trademark of Far Future Enterprises.
#

from rpg_tools.diceroll import roll
import os
import logging

from testing import testing

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'TravLITE 0.0.1'
__version__ = '0.0.1'


def app():

    def pick_sound(s_type):
        if s_type == V:
            sound = v_sounds[randint(1, len(v_sounds)) - 1]
        if s_type == CV:
            sound = ic_sounds[randint(1, len(ic_sounds)) - 1] + v_sounds[randint(1, len(v_sounds)) - 1]
        if s_type == VC:
            sound = v_sounds[randint(1, len(v_sounds)) - 1] + fc_sounds[randint(1, len(fc_sounds)) - 1]
        if s_type == CVC:
            sound = ic_sounds[randint(1, len(ic_sounds)) - 1] + v_sounds[randint(1, len(v_sounds)) - 1] \
            + fc_sounds[randint(1, len(fc_sounds)) - 1]
        if s_type == CC:
            sound = mc_sounds[randint(1, len(mc_sounds)) - 1]

    # UPP Code Table

    hex_code = ['0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'J', 'K',
                'L', 'M', 'N', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    noble_hex_code = ['0', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', 'A', 'B', 'c', 'C',
                      'D', 'e', 'E', 'f', 'F', 'G',
                      'G', 'H', 'H', 'H', 'H', 'H',
                      'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
    
    career = ['Agent', 'Army', 'Citizen', 'Drifter', 'Entertainer', 'Marines', 'Merchants', 'Navy', 'Nobility',
                  'Rogue', 'Scholar', 'Scout', 'Psion']
    career_count = len(career)
    left_career = []
    
    social_standing_male = ['NOT USED','NOT USED','NOT USED','NOT USED','NOT USED','NOT USED',
                            'NOT USED','NOT USED','NOT USED','NOT USED','NOT USED',
                            'Sir','Baronet','Baron','Marquis','Viscount','Count','Duke','Duke',
                            'Archduke','Prince','Emperor',
                            'Emperor','Emperor','Emperor','Emperor','Emperor','Emperor',
                            'Emperor','Emperor','Emperor','Emperor','Emperor','Emperor']

    social_standing_female = ['NOT USED','NOT USED','NOT USED','NOT USED','NOT USED','NOT USED',
                              'NOT USED','NOT USED','NOT USED','NOT USED','NOT USED',
                              'Lady','Baronetess','Baroness','Marchioness','Viscountess','Countess','Duchess','Duchess',
                              'Archduchess','Princess','Empress',
                              'Empress','Empress','Empress','Empress','Empress','Empress',
                              'Empress','Empress','Empress','Empress','Empress','Empress']
    
    social_class = ['Outcast',
                    'Misfit',
                    'Dregs of Society',
                    'Lower Low',
                    'Middle Low',
                    'Upper Low',
                    'Low Middle',
                    'Middle',
                    'Upper Middle',
                    'Low Upper',
                    'Middle Upper',
                    'Upper Upper',
                    'Remarkable',
                    'Extraordinary',
                    'Extreme',
                    'Supreme']
                             
    Agent = 0
    Army = 1
    Citizen = 2
    Drifter = 3
    Entertainer = 4
    Marines = 5
    Merchants = 6
    Navy = 7
    Nobility = 8
    Rogue = 9
    Scholar = 10
    Scout = 11
    Psion = 12
    
    # Characteristic Names
    
    characteristic_name = ['STR', 'DEX', 'END', 'INT', 'EDU', 'SOC']
    
    # Sound Tables

    V   = 1
    CV  = 2
    VC  = 3
    CVC = 4
    CC  = 5
    
    ic_sound = ['b','br','c','ch','d','g',
                     'h','j','k','l','m','p',
                     'r','s','st','sh',
                     't','v','w','z']
    ic_freq = [28,12,20,16,27,9,20,20,13,
                    28,24,27,24,30,13,25,
                    20,6,16,4]
    
    v_sound = ['a','e','i','o','u']
    v_freq = [16,20,10,7,3]

    mc_sound = ['g','lt','ns','nst','ls','ll','nn']
    mc_freq = [20,3,18,16,18,4,3]

    fc_sound = ['ch','ck','d','dy','dyne',
                     'hl','li','la','le','ler',
                     'nn','m','man','ma','mer','ny',
                     'me','n','nas','ne','ng',
                     'ner','nor','nie',
                     'rie','rlie','rly','rie','rt',
                     'ry','sa','sha','nshi','nski','son',
                     'nson','th','ta','ti','t','v',
                     'za','ue','than',
                     'lam','lis','lus','ton','tis','tus',
                     'love','se','nter','ll']
    fc_freq = [6,13,22,12,3,3,3,10,6,10,7,
                    25,10,4,13,12,5,27,11,4,14,13,17,7,6,5,5,6,3,
                    21,10,3,8,3,20,9,14,10,16,11,8,6,8,10,7,6,5,7,7,4,
                    4,12,5,4]
    
    for i in range(len(ic_sound)):
        log.debug(ic_sound[i] + ' ' + str(ic_freq[i]))
    
    for i in range(len(v_sound)):
        log.debug(v_sound[i] + ' ' + str(v_freq[i]))
        
    for i in range(len(mc_sound)):
        log.debug(mc_sound[i] + ' ' + str(mc_freq[i]))

    for i in range(len(fc_sound)):
        log.debug(fc_sound[i] + ' ' + str(fc_freq[i]))

    syllable_type = [V,V,V,V,V,V,V,V,VC,VC,VC,VC,CV,CV,CV,CV,CVC,CVC,CVC,CVC,CVC,CVC,CC,CC]
    #print syllable_type
    
    # Gen 10 NPCs
    
    for i in range(10):
        characteristic = {}
        #
        # Create a dictionary for the NPC's characteristics.
        # I could have used a list instead of a dict, but I
        # wanted to learn how to do dict for a change.
        #
        for key in characteristic_name:
            characteristic[key] = roll('2d6') # two 6-sided dice
        print characteristic
        

#
# Program exits here!
#


    
    


if __name__ == '__main__':
    
    log = logging.getLogger('TravLITE_' + __version__)
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/TravLITE.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                                  datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    
    log.info('Logging started.')
    log.info(__app__ + ' starting...')
    print
    print 'Thank you for giving', __app__, 'a try.'
    vernum, release = roll('info')
    print 'This program uses', release
    print
    print '----------------------------'
    print __author__
    print
    
    log.info(__app__ + ' started, and running...')
    
    app()