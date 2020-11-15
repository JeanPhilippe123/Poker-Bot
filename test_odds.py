"""
Auteur: Jean-Philippe Langelier 
Étudiant à la maitrise 
Université Laval
"""

from poker import Range
from poker.hand import Combo

import holdem_calc
import holdem_functions

board = ["Qc", "Th", "9s"]
villan_hand = None
exact_calculation = True
verbose = True
num_sims = 1
read_from_file = None

hero_hand = Combo('KsJc')

odds = holdem_calc.calculate_odds_villan(board, exact_calculation, 
                        num_sims, read_from_file, 
                        hero_hand, villan_hand, 
                        verbose, print_elapsed_time = True)