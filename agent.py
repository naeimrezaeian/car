import numpy as np 

class QAgent:
    def __init__(self,alpha,gamma,episodes,states,actions):
        self.alpha =  alpha
        self.gamma = gamma
        self.episodes = episodes
        self.states = states
        self.actions = actions

       def trainig(self):
           pass

        def get_actions(self):
            return np.random.randint(0,len(self.actions))

