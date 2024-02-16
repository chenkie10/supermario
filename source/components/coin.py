import pygame
from .. import tools, setup
from .. import constants as C


class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frames_index = 0
        frame_rects = [(1, 160, 5, 8), (9, 160, 5, 8), (17, 160, 5, 8), (9, 160, 5, 8)]
        self.load_frame(frame_rects)
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 58
        self.timer = 0

    def load_frame(self, frame_rects):
        sheet = setup.GRAPHICS['item_objects']
        for frame_rect in frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, (0, 0, 0), C.BG_MULTI))

    def update(self):
        self.current_time = pygame.time.get_ticks()
        frame_duration = [375, 125, 125, 125]

        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_duration[self.frames_index]:
            self.frames_index += 1
            self.frames_index %= 4
            self.timer = self.current_time

        self.image = self.frames[self.frames_index]
