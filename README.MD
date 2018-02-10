# NLP HMM Decoding: Viterbi algorithm

## what’s this
This is my [homework 2 from CS6320 in the University of Texas at Dallas, Spring 2018](http://www.hlt.utdallas.edu/~moldovan/CS6320.18S/Homework%202.pdf)

As well as published in [my Github](https://github.com/fatliau/NLP_HMM_Viterbi)

A Hidden Markov Model is an extension of a Markov chain in which the input symbols are not the same as the states.

Viterbi algorithm computes a trellis using dynamic programming.
Observation is processed from left to right filling out a trellis of states
with the probability that HMM is in state given seeing the previous observations.
![HMM](https://github.com/fatliau/NLP_HMM_Viterbi/HMM_weather.png)

## set up
1. environment: Python 3

## execute command
python Viterbi.py "WCWWSSCWC"
(python Viterbi.py <String action>)

## assumption
1. hard-code the probability of: 1.weather start 2.weather-weather 3.weather-action.

## result example
```
JCMacBook:HW2 JC$ python Viterbi.py "WCWWSSCWC"
```
```
RRSSSSRRR
```
