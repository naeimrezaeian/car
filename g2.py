import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
import numpy as np

actions=["Up","Down","Space"]
num_feats=3
class Car:
    def __init__(self, x, y, angle=0.0, length=4,  max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2

        self.acceleration = 0.0
        self.steering = 0.0

    def update(self, dt):
        
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))
        self.position += self.velocity.rotate(-self.angle) * dt

    def step(self,action,dt):
        
        if action=="UP":
            
            if self.velocity.x < 0:
                self.acceleration = self.brake_deceleration
            else:
                self.acceleration += 1 * dt

        elif action=="DOWN":
            
            if self.velocity.x > 0:
                self.acceleration = -self.brake_deceleration
            else:
                self.acceleration -= 1 * dt

        elif action=="SPACE":
            
            if abs(self.velocity.x) > dt * self.brake_deceleration:
                self.acceleration = -copysign(self.brake_deceleration, self.velocity.x)
            else:
                self.acceleration = -self.velocity.x / dt
        else:
            if abs(self.velocity.x) > dt * self.free_deceleration:
                self.acceleration = -copysign(self.free_deceleration, self.velocity.x)
            else:
                if dt != 0:
                    self.acceleration = -self.velocity.x / dt

        self.acceleration = max(-self.max_acceleration, min(self.acceleration, self.max_acceleration))
        self.update(dt)
        

class Agent():
    
    self.weights = np.array([0 for x in range(num_feats)])
    
    self.gamma = 0.9
    self.alpha = 0.005
    self.explore = 0

    def __init__(self):
        print("init")
     def getFeature(self, s, a):
        """ returns feature value calculation of a q-state
        1. Distance
        2. Velocity
        3. Time"""
        feature_vector = []

        return np.array(feature_vector)

    def getQValue(self, s, a):
        """ returns dot-product of feature vector with weight vector """
        return sum(self.weights * self.getFeature(s, a))

    def update(self, s1, a, s2, r):
        """ updates weights based on transition """
        diff = r + (self.gamma * max([self.getQValue(s2, act) for act in actions])) - self.getQValue(s1, a)
        self.weights = self.weights + (self.alpha * diff * self.getFeature(s1, a))


    def AgentAction(self):


    def run(self):
        pass













if __name__ == '__main__':
    agent = Agent()
    agent.run()