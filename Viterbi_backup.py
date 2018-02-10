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
import operator

weather = {"R":{"R":0.6, "S":0.4}, "S":{"R":0.3,"S":0.7}}
print(weather)
print(weather["R"]["S"])
print(weather["S"]["R"])

action = {"R":{"W":0.3,"S":0.35,"C":0.35}, "S":{"W":0.5,"S":0.4,"C":0.1}}
print(action)
print(action["R"]["W"])
print(action["S"]["C"])

start = {"R":0.7, "S":0.3}

def recursiveViterbi():
    actRecord = list("WC")
    weaGuess = {}
    #base step
    for w in start.keys():
        act = actRecord[0]
        weaGuess[w] = start[w] * action[w][act]
    #second step
    wkList = copy.deepcopy(list(weaGuess.keys()))
    for wk in wkList:
        w = list(wk)
        #print(w,w[-1])
        act = actRecord[1]
        for today_w in weather.keys():
            new_w = wk+today_w
            #print("# ",wk, today_w)
            #print(weaGuess[wk] , weather[w[-1]][today_w] , action[today_w][act])
            weaGuess[new_w] = weaGuess[wk] * weather[w[-1]][today_w] * action[today_w][act]
        del weaGuess[wk]
    print(weaGuess)
   
    
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
            
            
recursiveViterbi()
viterbi("WC")

result = viterbi("WCWWS")
print(result.keys())
sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_result)



sorted2_result = sorted(result.items(), key=lambda x: x[1])
print(sorted2_result)

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
sorted2_x = sorted(x.items(), key=lambda x: x[1])
print(sorted2_x)
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print(sorted_x)
sorted2_x = sorted(x.items(), key=lambda x: x[0])
print(sorted2_x)
#viterbi("WCWWSSCWC")




"""
word="hello"
print(list(word)[-1])
"""