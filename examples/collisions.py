import pymunk
import pygame


class ReactiveCircle:
    def __init__(self, space, start_x, start_y, r, velocity=(0, 0), density=1, elasticity=1, collision_type=1):
        self.r = r
        self.body = pymunk.Body()
        self.body.position = start_x, start_y
        self.body.velocity = velocity
        self.shape = pymunk.Circle(self.body, self.r)
        self.shape.density = density
        self.shape.mass = 1000
        self.shape.elasticity = elasticity
        space.add(self.body, self.shape)
        self.shape.collision_type = collision_type

    def draw(self, surface, color, offset):
        pygame.draw.circle(surface, color,
                           (int(self.body.position[0] - int(offset[0]) + 15),
                            int(self.body.position[1] - int(offset[1]) + 15)),
                           self.r)


class StaticPoly:
    def __init__(self, space, pos, elasticity=0, collision_type=None):
        self.pos = pos
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Poly(self.body, self.pos)
        self.shape.elasticity = elasticity
        if collision_type:
            self.shape.collision_type = collision_type
        space.add(self.body, self.shape)

    def draw(self, surface, color, offset):
        imx, imy = offset
        dep = [(x[0] - imx + 15, x[1] - imy + 15) for x in self.pos]
        pygame.draw.polygon(surface, color, dep)


class KinematicRect:
    def __init__(self, space, pos, collision_type=1):
        self.pos = pos
        self.r = 15
        self.body = pymunk.Body()
        self.body.position = pos[0], pos[1]
        self.body.velocity = [0, 0]
        self.shape = pymunk.Poly.create_box(self.body, (pos[2], pos[3]))
        self.shape.density = 10
        self.shape.mass = 10000000
        self.shape.elasticity = 0
        space.add(self.body, self.shape)
        self.shape.collision_type = collision_type
        self.jumping = False

    def just_call_me(self):
        pass

    def draw(self, surface, color, x, y):
        pygame.draw.rect(surface, color, (x, y, self.pos[2], self.pos[3]))

    def continue_jump(self, speed_y):
        self.jumping = True
        self.body.velocity = self.body.velocity[0], speed_y

    def move(self, speed_x):
        self.body.velocity = speed_x, self.body.velocity[1]
