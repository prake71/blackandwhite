import pygame

class CustomScene(object):

    def __init__(self, text):
        self.text = text
        super(CustomScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 56)

    def render(self, screen):
        # ugly!
        screen.fill((0, 200, 0))
        text1 = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text1, (200, 50))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                self.manager.go_to(TitleScene())

