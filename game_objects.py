from ursina import *
from random import randrange
from ursina.shaders import lit_with_shadows_shader


class Apple(Entity):
    def __init__(self, MAP_SIZE, **kwargs):
        super().__init__(**kwargs)
        self.MAP_SIZE = MAP_SIZE
        self.new_position()

    def new_position(self):
        self.position = (randrange(self.MAP_SIZE) + 0.5, randrange(self.MAP_SIZE) + 0.5, -0.5)

class Snake:
    def __int__(self, MAP_SIZE):
        self.MAP_SIZE = MAP_SIZE
        self.segment_length = 1
        self.position_lenght = self.segment_length +1
        self.segment_position = [Vec3(randrange(MAP_SIZE) + 0.5, randrange(MAP_SIZE) + 0.5, -0.5)]
        # self.segment_entities = [Entity(model='sphere', color=color.green, position=self.segment_position[0])]
        self.segment_entities = []
        self.create_segment(self.segment_position[0])
        self.directions = {'a': Vec3(-1, 0, 0), 'd': Vec3(1, 0, 0), 'w': Vec3(0, 1, 0), 's': Vec3(0, -1, 0)}
        self.direction = Vec3(0, 0, 0)
        self.permissions = {'a': 1, 'd': 1, 'w': 1, 's': 1}
        self.taboo_movement = {'a': 'b', 'd': 'a', 'w': 's', 's': 'w'}
        self.speed, self.score = 12, 0
        self.frame_counter = 0

    def add_segment(self):
        self.segment_length += 1
        self.position_lenght += 1
        self.score += 1
        self.speed = max(self.speed - 1, 5)
        self.create_segment(self.segment_position[0])

    def create_segment(self, position):
        entity = Entity(self, position)
        Entity(model='sphere', color=color.green, position=position).add_script(
            SmoothFollow(speed=12, target=entity, offset=(0, 0, 0)))
        self.segment_entities.insert(0, entity)

    def run(self):
        self.frame_counter += 1
        if not  self.frame_counter % self.speed:
            self.control()
            self.segment_entities.append(self.segment_positions[-1] + self.direction)
            self.segment_positions = self.segment_positions[-self.segment_length:]
            for segment, segment.position in zip(self.segment_entities, self.segment_positions):
                segment.position = segment.position

    def control(self):
        for key in 'wasd':
            if held_keys[key] and self.permissions[key]:
                self.direction = self.directions[key]
                self.directions = dict.fromkeys(self.permissions, 1)
                self.directions[self.taboo_movement[key]] = 0
                break