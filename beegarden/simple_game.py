# -*- coding: utf-8 -*-
"""simple game example"""

from beegarden.core import Beegarden
from beegarden.my_bee import MyBee

if __name__ == '__main__':
    scene = Beegarden(
        name="My little garden",
        flowers_count=5,
        theme_mod_path='beegarden.themes.for_test',
    )
    bee = MyBee()  # bee born
    bee1 = MyBee()

    scene.go()  # let the world revolves around you
