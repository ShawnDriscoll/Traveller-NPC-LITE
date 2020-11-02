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

__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'
__app__ = 'TravLITE 0.0.1'
__version__ = '0.0.1'


def app():
    print roll('2d6')
    
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