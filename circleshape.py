import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        #this works but you can call pygame.Vector2.distance_to with just the position variable
        #and .distance_to with the other.position as the argument. The if else statement is also
        #unecessary as everything can be rolled into a return statement.
        #    --------------------------------------------------------------
        #distance = pygame.Vector2.distance_to(self.position, other.position)
        #if distance < self.radius + other.radius:
            #return True
        #else:
            #return False
        #    --------------------------------------------------------------

        return self.position.distance_to(other.position) <= self.radius + other.radius