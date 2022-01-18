import pygame as pygame
from COE.UI.text import text


class Item:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.colour1 = (205, 133, 63)
        self.colour2 = (128, 128, 128)
        # information game
        self.resouces_surface = pygame.Surface((width, height * 0.02))
        self.resouces_surface.fill(self.colour1)
        # frame to choose
        self.select_surface = pygame.Surface((width, height * 0.25))
        self.select_surface.fill(self.colour1)
        # frame of items
        self.build_surface = pygame.Surface((width * 0.6, height * 0.25))
        self.build_surface.fill(self.colour2)
        self.images = self.load_images()
        self.cells = self.create_build_item()
        self.selected_cell = None

    def create_build_item(self):
        render_pos = [self.width * 0.15 + 10, self.height * 0.74 + 10]
        object_width = self.build_surface.get_width() // 10  # size of item
        cells = []
        for image_name, image in self.images.items():
            pos = render_pos.copy()
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, w=object_width)
            rect = image_scale.get_rect(topleft=pos)
            cells.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": self.images[image_name],
                    "rect": rect,
                }
            )
            render_pos[0] += image_scale.get_width() + 10  # Distance between 2 elements
        return cells

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        if mouse_action[2]:
            self.selected_cell = None
        for cell in self.cells:
            if cell["rect"].collidepoint(mouse_pos):
                if mouse_action[0]:
                    print("Item is picked")
                    self.selected_cell = cell

    def draw_item(self, screen):
        if self.selected_cell is not None:
            img = self.selected_cell["image"].copy()
            img.set_alpha(100)
            screen.blit(img, pygame.mouse.get_pos())

        screen.blit(self.resouces_surface, (0, 0))
        # frame
        screen.blit(self.select_surface, (0, self.height * 0.74))
        # frame 2
        screen.blit(self.build_surface, (self.width * 0.15, self.height * 0.74))
        for cell in self.cells:
            screen.blit(cell["icon"], cell["rect"].topleft)

        pos1 = self.width * 0.05
        for resource in ["Wood:", "Meat:", "Gold:", "Stone:"]:
            text(screen, resource, 25, (255, 255, 255), (pos1, 0))
            pos1 += 100

        pos2 = self.width * 0.5
        text(screen, "Stone Age", 25, (255, 255, 255), (pos2, 0))

    def load_images(self):
        building1 = pygame.image.load("COE/assets/building01.png")
        building2 = pygame.image.load("COE/assets/building02.png")
        building3 = pygame.image.load("COE/assets/building03.png")
        images = {
            "building1": building1,
            "building2": building2,
            "building3": building3,
        }
        return images

    def scale_image(self, image, w=None, h=None):
        if (w is None) and (h is None):
            pass
        elif h is None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pygame.transform.scale(image, (int(w), int(h)))
        elif w is None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pygame.transform.scale(image, (int(w), int(h)))
        else:
            image = pygame.transform.scale(image, (int(w), int(h)))
        return image
