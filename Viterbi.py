#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 10:21:19 2018

@author: JC

Homework 2
Due 2/19/2018
HMM Decoding: Viterbi Algorithm

Implement the Viterbi algorithm and run it with the HMM in Figure 1 to compute the most likely weather sequence.

Figure 1. A Hidden Markov Model for relating action (Walk, Shop and Clean, the observations) to weather (Rainy or Sunny, the hidden variables). For this example, we are not using an end-state, instead allowing both states Rainy and Sunny to be a final (accepting) state.

1. The observation sequences (input sequence) could be any length from 1 to 10.
2. You can hard code the HMM in Figure 1 inside the program, but do not hard code the observation sequence (input sequence).
3. Program from scratch, do not use any high-level package that already contains the algorithm.
4. Command Line: Python Viterbi.py <sequence>

Example of input/output:
Observation (input): WCWWSSCWC (Command line: Python Viterbi.py “WCWWSSCWC”)
W-Walk, C-Clean, S-Shop
Weather (output): RRSSSSRRR
R-Rainy, S-Sunny
"""
import copy
import sys

weather = {"R":{"R":0.6, "S":0.4}, "S":{"R":0.3,"S":0.7}}
action = {"R":{"W":0.3,"S":0.35,"C":0.35}, "S":{"W":0.5,"S":0.4,"C":0.1}}
start = {"R":0.7, "S":0.3}

def main():
    if len(sys.argv) != 2:
        print("Argument format dismatch! Correct form as: python Viterbi.py <actions>")
    else:
        weaGuess = viterbi(sys.argv[1])
        wea_sorted = sorted(weaGuess.items(), key = lambda x:x[1], reverse=True)
        print(wea_sorted[0][0])
        
def viterbi(record):
    actRecord = list(record)
    weaGuess = {}
    #first day
    for w in start.keys():
        act = actRecord[0]
        weaGuess[w] = start[w] * action[w][act]
    #other days
    for day in range(1,len(actRecord)):
        wGuessList = copy.copy(list(weaGuess.keys()))
        for wk in wGuessList:
            w = list(wk)[-1]
            act = actRecord[day]
            for today_w in weather.keys():
                new_w = wk+today_w
                weaGuess[new_w] = weaGuess[wk] * weather[w][today_w] * action[today_w][act]
            del weaGuess[wk]
    return weaGuess
            
if __name__ == '__main__':
    main()
 
#python Viterbi.py "WCWWSSCWC"
