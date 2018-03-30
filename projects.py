import os, sys, imp

#sys.path.append('/home/ubuntu/workspace/random_code')
sys.path.append('../random_code')
#sys.path.append('../monopoly-sim')

from collatzConjecture import calculateCollatz

from fizzbuzz import selectMethod

from monopoly_sim.monopoly import calculateGames
#import monopoly.calculateGames from calculateGames

#from hoffmanCoding import encode

#from ...random_code import collatzConjecture

#collatzConjecture = imp.load_source('~/workspace/random-code/collatzConjecture.py')

# Now you can import your module
#import collatzConjecture


#TODO: figure out how to make python scripts ask for inputs if run from the CLI, or just accept values if called as a function

def collatz(limit):
    
    return calculateCollatz(limit)
    
# def hoffman(string):
#     return encode(string)
    
def fizzbuzz(method, limit):
    return selectMethod(method, limit)
    
def monopoly(gamesCount):
    return calculateGames(int(gamesCount))