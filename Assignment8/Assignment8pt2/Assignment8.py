from HMMfunc import *
import operator

prob = HMMfunc("typos20.data", "typos20Test.data")
prob.calcocc()
prob.calcprob()
prob.printdata()
prob.Viterbi()
#prob.printpath()

