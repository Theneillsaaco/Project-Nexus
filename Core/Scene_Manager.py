import pygame

class SceneManager:
    def __init__(self):
        self.scenes = []

    def push(self, scene):
        self.scenes.append(scene)

    def pop(self):
        if self.scenes:
            self.scenes.pop()

    def replace(self, scene):
        self.pop()
        self.push(scene)

    def handle_event(self, event):
        if self.scenes:
            self.scenes[-1].handle_event(event)

    def update(self, dt):
        if self.scenes:
            self.scenes[-1].update(dt)

    def draw(self):
        if self.scenes:
            self.scenes[-1].draw()