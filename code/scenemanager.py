from titlescene import *

class SceneManager(object):
    def __init__(self):
        pass

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
