import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
import numpy as np


class Car:
    def __init__(self, x, y, angle=0.0, length=4, max_steering=30, max_acceleration=5.0):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2

        self.acceleration = 0.0
        self.steering = 0.0

    def update(self, dt):
        
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car tutorial")
        width = 1000
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
        self.runtime=0
        self.actions=["UP","DOWN","SPACE"]
        self.actions=["UP","UP","UP"]
        self.car=0
    def step(self,action,dt):
        # User input
        
        
        if self.actions[action]=="UP":
            
            if self.car.velocity.x < 0:
                self.car.acceleration = self.car.brake_deceleration
            else:
                self.car.acceleration += 1 * dt
        elif self.actions[action]=="DOWN":
            
            if self.car.velocity.x > 0:
                self.car.acceleration = -self.car.brake_deceleration
            else:
                self.car.acceleration -= 1 * dt
        elif self.actions[action]=="SPACE":
            
            if abs(self.car.velocity.x) > dt * self.car.brake_deceleration:
                self.car.acceleration = -copysign(self.car.brake_deceleration, self.car.velocity.x)
            else:
                self.car.acceleration = -self.car.velocity.x / dt
        else:
            if abs(self.car.velocity.x) > dt * self.car.free_deceleration:
                self.car.acceleration = -copysign(self.car.free_deceleration, self.car.velocity.x)
            else:
                if dt != 0:
                    self.car.acceleration = -self.car.velocity.x / dt
        self.car.acceleration = max(-self.car.max_acceleration, min(self.car.acceleration, self.car.max_acceleration))


    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        self.car = Car(2, 5)
        ppu = 32
        current_time=0
        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            get_action=np.random.randint(3)    
            print(get_action)
            self.step(get_action,dt)
            # Logic
            self.car.update(dt)
            font = pygame.font.SysFont(None, 24)
            txt=str("Acceleration:"+str(self.car.acceleration)[:3]+" Steering:"+str(self.car.steering)[:3]+" Velocity:"+str(self.car.velocity[0])[:3])
            text1 = font.render(txt, True, (255,0,0))
            text2 = font.render((str(self.car.position)), True, (255,0,0))
            
            # Drawing
            self.screen.fill((0, 0, 0))
            rotated = pygame.transform.rotate(car_image, self.car.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, self.car.position * ppu - (rect.width / 2, rect.height / 2))
            self.screen.blit(text1, (10, 50))
            self.screen.blit(text2, (10, 70))
            pygame.display.flip()
            current_time=pygame.time.get_ticks()
            self.runtime=current_time/1000
            if round(self.car.position[0])==15:
                print(self.runtime)
                self.exit = True
                

            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()