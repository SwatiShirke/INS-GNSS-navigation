# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:14:34 2023
@author: swati shirke 
"""

actions = ['push','do_nothing']
states = ['open', 'closed']
no_actions = len(actions)
no_states = len(states)


state_probabilities = {'open':0.5, 'closed':0.5}
#print(state_probabilities['open'])
##measurement_prob is a 2d dictionary of (state,measurement) probabilities
measurement_prob = {'open':{'open':0.6,'closed':0.4}, 'closed': {'open':0.2 ,'closed':0.8}}
##print(measurement_prob['open']['closed'])

##state transition probabilities[state][action][next_state] -- prob of next_state while state and action is given
state_transition_prob = {'open':{'pull':{'open':1.0,'closed':0.0} ,'do_nothing':{'open':1.0,'closed':0.0}} ,
                         'closed':{'pull':{'open':0.8,'closed':0.2} ,'do_nothing':{'open':0.0,'closed':1.0}}}

belief_prob = {'open':0.5,'closed':0.5}
pred_prob = {'open':0.5,'closed':0.5}

##print(state_transition_prob['open']['do_nothing']['open'])
##action, state list 
action_measurement = [['do_nothing','closed',],
                      ['do_nothing', 'closed'],
                      ['pull', 'closed'],
                      ['pull','open'],
                      ['do_nothing','open']]
##Bayes filtering
for i in range(len(action_measurement)):
     action = action_measurement[i][0]     
     measurement = action_measurement[i][1]       
     print("action=", action, ", measurement=", measurement)
     for j in range(no_states):
         next_state = states[j] 
         #print(next_state)
         ##predict
         next_state_total_prob = 0
         for k in range(no_states):
             current_state =  states[k]
             next_state_total_prob = next_state_total_prob +  state_transition_prob [current_state][action][next_state] * belief_prob[current_state]
         pred_prob[next_state] =  next_state_total_prob
         #print(pred_prob)
     ##print("here>>>>>>>>>>>>>>>")
      
         #correct
     sum = 0 
     for l in range(no_states):
         current_state = states[l]
         prob =  measurement_prob[current_state][measurement]  * pred_prob[current_state] 
         belief_prob[current_state] = prob 
         sum = sum + prob
     neeta = pow(sum,-1)
     
     for m in range(no_states):
         current_state = states[m]
         belief_prob[current_state] = neeta * belief_prob[current_state]
         
     #sum = sum + belief_prob 
     print("belief probability")
     print(belief_prob)
     print("************************************")
         
     
     
     


                         
                         
      
