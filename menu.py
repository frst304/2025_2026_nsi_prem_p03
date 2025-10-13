import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'user_actions'))

from login import login_fctn

from display_menu import display_menu_fctn

from view_sold import view_sold_fctn # type: ignore
from pull_money import pull_money_fctn # type: ignore
from add_money import add_money_fctn # type: ignore

def menu_fctn():
    user = login_fctn()
    os.system('cls')
    display_menu_fctn(user)
