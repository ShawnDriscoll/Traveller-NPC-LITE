#
#   diceroll.py
#
#   Written for Classic Python 2.5.4
#
#   To use this module: from diceroll import roll
#
#   Make a dice roll
#
##########################################################

'''
diecroll module containing roll()

Usage:
    from diceroll import roll
    print roll('2D6')

    Will roll two 6-sided dice, returning an integer
'''

from random import randint
import os
import logging
import sys
from colorama import init
from colorama import Fore, Back, Style

init() # initialize colorama

__version__ = '3.1'
__release__ = '3.1.0b'
__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'

diceroll_log = logging.getLogger('diceroll')
diceroll_log.setLevel(logging.INFO)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

fh = logging.FileHandler('Logs/diceroll.log', 'w')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                              datefmt = '%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
diceroll_log.addHandler(fh)

diceroll_log.info('Logging started.')
diceroll_log.info('roll() v' + __version__ + ' started, and running...')

number_of_dice = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
simple_dice = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D30']
traveller5_dice = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D']

def _dierolls(dtype, dcount):
    '''
    Takes two integer arguments:
        dtype (the number of sides for the dice)
        dcount (the number of dice to roll)
    
    and returns an integer value.
    
    This function is for internal use and has no error-checking!    
    '''

    dtotal = 0
    if dcount == 1:
        diceroll_log.debug('Using %s %d-sided die...' % (number_of_dice[dcount], dtype))
    else:
        if dcount < 11:
            diceroll_log.debug('Using %s %d-sided dice...' % (number_of_dice[dcount], dtype))
        else:
            diceroll_log.debug('Using %d %d-sided dice...' % (dcount, dtype))
        
    for i in range(dcount):
        rolled = randint(1, dtype)
        if rolled == 8 or rolled == 11 or rolled == 18 or rolled >= 80 and rolled <= 89:
            diceroll_log.debug('Rolled an %s' % rolled)
        else:
            diceroll_log.debug('Rolled a %s' % rolled)
        dtotal += rolled
    return dtotal

def roll(dice):
    '''
    The dice types to roll are:
        '4dF', 'D2', 'D3', 'D4', 'D6', 'D8', 'D09', 'D10',
        'D12', 'D20', 'D30', 'D099', 'D100', 'D66', 'DD',
        'FLUX', 'GOODFLUX', 'BADFLUX', 'BOON', 'BANE',
        and also Traveller5's 1D thru 10D rolls

    Some examples are:
    roll('D6') or roll('1D6') -- roll one 6-sided die
    roll('2D6') -- roll two 6-sided dice
    roll('D09') -- roll a 10-sided die (0 - 9)
    roll('D10') -- roll a 10-sided die (1 - 10)
    roll('D099') -- roll a 100-sided die (0 - 99)
    roll('D100') -- roll a 100-sided die (1 - 100)
    roll('D66') -- roll for a D66 chart
    roll('FLUX') -- a FLUX roll (-5 to 5)
    roll('3D6+6') -- add +6 DM to roll
    roll('4D4-4') -- add -4 DM to roll
    roll('2DD+3') -- roll (2D6+3) x 10
    roll('BOON') -- roll 3D6 and keep the higher two dice
    roll('4dF') -- make a FATE roll
    roll('4D') -- make a Traveller5 4D roll
    roll('info') -- release version of program
    
    An invalid roll will return a 0.
    '''

    log = logging.getLogger('your_code_name_here.diceroll')

    # make inputted string argument upper case, and remove spaces
    dice = str(dice).upper().replace(' ','')
    
    # was information for this program asked for?
    if dice == 'INFO':
        ver = 'roll(), release version ' + __release__ + ' for Classic Python 2.5.4'
        diceroll_log.info('Reporting: roll() release version: %s' % __release__)
        return __version__, ver
    
    # was a test asked for?
    if dice == 'TEST':
        diceroll_log.info('A 6x6 test was started...')
        roll_chart_6x6 = {}
        data = []
        for i in range(13):
            data.append(0)
        n = 10000
        
        for i in range(6):
            for j in range(6):
                roll_chart_6x6[(i+1, j+1)] = 0
        print
        print '      6x6 Roll Chart Test'
        print '     1    2    3    4    5    6'     
        for i in range(n):
            die1 = _dierolls(6, 1)
            die2 = _dierolls(6, 1)
            roll_chart_6x6[(die1, die2)] += 1
            result = die1 + die2
            data[result] += 1
                
        for i in range(6):
            print i+1,
            for j in range(6):
                print '%4d' % roll_chart_6x6[(i+1, j+1)],
            print
        
        for i in range(6):
            for j in range(6):
                roll_chart_6x6[(i+1, j+1)] = 0
        print
        print '            6x6 Roll Chart Percentage'
        print '        1       2       3       4       5       6'
        for x in range(13):
            if x > 1:
                for i in range(6):
                    for j in range(6):
                        if (i+1)+(j+1) == x and roll_chart_6x6[(i+1, j+1)] == 0:
                            roll_chart_6x6[(i+1, j+1)] = data[x]
        
        for i in range(6):
            print i+1,
            for j in range(6):
                print '%6.2f%%' % (roll_chart_6x6[(i+1, j+1)] * 100. / n),
            print
        print
        diceroll_log.info('6x6 test completed 100%.')
        for x in range(len(data)):
            data[x] = data[x] * 100. / n
        return data[2:13]

    log.debug(dice)
    diceroll_log.debug('Asked to roll %s:' % dice)

    # set dice modifier to zero.
    dice_mod = 0

    # check if a FATE dice roll
    if dice == '4DF':
        fate1 = _dierolls(3, 1) - 2
        fate2 = _dierolls(3, 1) - 2
        fate3 = _dierolls(3, 1) - 2
        fate4 = _dierolls(3, 1) - 2
        rolled = fate1 + fate2 + fate3 + fate4
        diceroll_log.info('%s = %d, %d, %d, %d = %d' % (dice, fate1, fate2, fate3, fate4, rolled))
        return rolled
    
    # check if FLUX dice are being rolled
    elif dice == 'FLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        rolled = flux1 - flux2
        diceroll_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled

    elif dice == 'GOODFLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        if flux1 < flux2:
            rolled = flux2 - flux1
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled

    elif dice == 'BADFLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        if flux1 > flux2:
            rolled = flux2 - flux1
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled

    # check if a BOON roll is being performed
    elif dice == 'BOON':
        die = [0, 0, 0]
        die[0] = _dierolls(6, 1)
        die[1] = _dierolls(6, 1)
        die[2] = _dierolls(6, 1)
        diceroll_log.info('Start Boon roll: %d %d %d' % (die[0], die[1], die[2]))
        die_swap = True
        while die_swap == True:
            die_swap = False
            for j in range(2):
                if die[j] < die[j+1]:
                    temp_die = die[j]
                    die[j] = die[j+1]
                    die[j+1] = temp_die
                    die_swap = True
        rolled = die[0] + die[1]
        diceroll_log.info('Sorted Boon roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled
    
    # check if a BANE roll is being performed
    elif dice == 'BANE':
        die = [0, 0, 0]
        die[0] = _dierolls(6, 1)
        die[1] = _dierolls(6, 1)
        die[2] = _dierolls(6, 1)
        diceroll_log.info('Start Bane roll: %d %d %d' % (die[0], die[1], die[2]))
        die_swap = True
        while die_swap == True:
            die_swap = False
            for j in range(2):
                if die[j] > die[j+1]:
                    temp_die = die[j]
                    die[j] = die[j+1]
                    die[j+1] = temp_die
                    die_swap = True
        rolled = die[0] + die[1]
        diceroll_log.info('Sorted Bane roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled
    
    else:
        # check if T5 dice are being rolled
        t5_dice = dice
        dice_mod = 0
        ichar2 = dice.find('+')
        if ichar2 <> -1:
            dice_mod = int(dice[ichar2:len(dice)])
            t5_dice = dice[0:ichar2]
        else:
            ichar2 = dice.find('-')
            if ichar2 <> -1:
                dice_mod = int(dice[ichar2:len(dice)])
                t5_dice = dice[0:ichar2]
        if t5_dice in traveller5_dice:
            num_dice = int(t5_dice[0:len(t5_dice) - 1])
            rolled = _dierolls(6, num_dice) + dice_mod
            diceroll_log.info('Traveller5 %s = %d%s+%d = %d' % (dice, num_dice, 'D6', dice_mod, rolled))
            return rolled

    # look for DD in the string (for destructive dice rolls)
    ichar1 = dice.find('DD')
    if ichar1 == -1:
        
        # if not, does the string indicate regular dice for use?
        ichar1 = dice.find('D')
    if ichar1 == 0:
        
        # only one die is being rolled
        num_dice = 1

    if ichar1 <> -1:
        if ichar1 <> 0:
            
            # how many dice are being rolled?
            num_dice = int(dice[0:ichar1])
            if num_dice < 1:
                if num_dice < 0:
                    log.error('Negative dice count! [ERROR]')
                diceroll_log.error('Number of dice = ' + str(num_dice) + ' [ERROR]')
    
        if num_dice >= 1:
            
            # is there a +/- dice modifier for the roll?
            ichar2 = dice.find('+')
            if ichar2 <> -1:
                dice_mod = int(dice[ichar2:len(dice)])
            else:
                ichar2 = dice.find('-')
                if ichar2 <> -1:
                    dice_mod = int(dice[ichar2:len(dice)])
    
            # what kind of dice are being rolled? D6? D66? etc.
            if ichar2 <> -1:
                dice_type = dice[ichar1:ichar2]
            else:
                dice_type = dice[ichar1:len(dice)]
            
            if dice_type in simple_dice:
                rolled = _dierolls(int(dice_type[1:len(dice_type)]), num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D2' and num_dice == 1 and dice_mod == 0:
                rolled = _dierolls(2, 1) - 1
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D66' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(6, 1)
                roll_2 = _dierolls(6, 1)
                rolled = roll_1 * 10 + roll_2
                diceroll_log.info('%s = %d%s+%d = %d and %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, rolled))
                return rolled
            elif dice_type == 'D09' and num_dice == 1:
                rolled = (_dierolls(10, 1) - 1) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D099' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1) - 1
                rolled = roll_1 + roll_2 + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d and %d + %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
            elif dice_type == 'D100' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1)
                rolled = roll_1 + roll_2 + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d and %d + %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
            elif dice_type == 'DD':
                rolled = (_dierolls(6, num_dice) + dice_mod) * 10
                diceroll_log.info('%s = (%d%s+%d) * 10 = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D00' and num_dice == 1:
                log.warning('D00 was deprecated in 1.9. Use D100 instead.')
                diceroll_log.warning('D00 was deprecated in 1.9. Use D100 instead.')
                print
                print Fore.YELLOW + Style.BRIGHT + 'WARNING: D00 was deprecated in 1.9. Use D100 instead.'
                print Fore.RESET + Back.RESET + Style.RESET_ALL
                dice_type = 'D100'
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1)
                rolled = roll_1 + roll_2 + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d and %d + %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
                                                    
    log.error('Wrong dice type entered! [ERROR]')
    diceroll_log.error('!!!!!!!!!!!!!!!!!!!!! DICE ERROR! ' + dice + ' is unknown !!!!!!!!!!!!!!!!!!!!!!!!!')
    
    print
    print Fore.RED + Style.BRIGHT + "** DICE ERROR! '%s' is unknown **" % dice
    print Fore.RESET + Back.RESET + Style.RESET_ALL
    print "Valid dice rolls are:"
    print "roll('D6') or roll('1D6') -- roll one 6-sided die"
    print "roll('2D6') -- roll two 6-sided dice"
    print "roll('D09') -- roll a 10-sided die (0 - 9)"
    print "roll('D10') -- roll a 10-sided die (1 - 10)"
    print "roll('D099') -- roll a 100-sided die (0 - 99)"
    print "roll('D100') -- roll a 100-sided die (1 - 100)"
    print "roll('D66') -- roll for a D66 chart"
    print "roll('FLUX') -- a FLUX roll (-5 to 5)"
    print "roll('2DD+3') -- roll (2D6+3) x 10"
    print "roll('BOON') -- roll 3D6 and keep the higher two dice"
    print "roll('4D') -- make a Traveller5 4D roll"
    print "roll('4dF') -- make a FATE roll"
    print
    print "-/+ DMs can be added to rolls:"
    print "roll('3D6+6') -- add +6 DM to roll"
    print "roll('4D4-4') -- add -4 DM to roll"
    print
    print "roll('info') -- release version of program"
    print
    return 0

if __name__ == '__main__':
    diceroll_log.info('diceroll was run without roll() called.  Help will be sent if needed.')
    print
    if len(sys.argv) < 2:
        print '     Type:'
        print "     'diceroll.py -h' for help"
        print "     'diceroll.py -v' for version"
    elif sys.argv[1] in ['-h', '/h', '--help', '-?', '/?']:
        print '     diceroll is a module (containing a roll function)'
        print '     that needs to be imported into Python.'
        print
        print '     For example:'
        print '     >>> import diceroll'
        print "     >>> print diceroll.roll('2d6')"
        print
        print '     Or:'
        print '     >>> from diceroll import roll'
        print "     >>> print roll('2d6')"
        print
        print
        print '     But, as a last resort:'
        print "     C:\>diceroll.py roll('2d6')"
        print
        print '     Or just:'
        print '     C:\>diceroll.py 2d6'
    elif sys.argv[1] in ['-v', '/v', '--version']:
        print '     roll(), release version ' + __release__ + ' for Classic Python 2.5.4'
    else:
        dice = sys.argv[1]
        if "roll('" in dice:
            num = dice.find("')")
            if num <> -1:
                dice = dice[6:num]
                dice = str(dice).upper().strip()            
                num = roll(dice)
                if dice <> 'TEST' and dice <> 'INFO':
                    print 'Your %s roll is %d.' % (dice, num)
                    diceroll_log.info('The direct call to diceroll with %s resulted in %d.' % (dice, num))
                elif dice == 'INFO':
                    print 'roll(), release version ' + __release__ + ' for Classic Python 2.5.4'
        else:
            dice = str(dice).upper().strip()
            num = roll(dice)
            if dice <> 'TEST' and dice <> 'INFO':
                print 'Your %s roll is %d.' % (dice, num)
                diceroll_log.info('The direct call to diceroll with %s resulted in %d.' % (dice, num))
            elif dice == 'INFO':
                    print 'roll(), release version ' + __release__ + ' for Classic Python 2.5.4'
