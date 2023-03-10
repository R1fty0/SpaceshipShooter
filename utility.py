import pygame


class Window:
    def __init__(self, window_fps, window_width, window_height, window_name, background_rgb: tuple):
        """ Contains attributes needed to run the game. """
        self.window_fps = window_fps
        self.window_width = window_width
        self.window_height = window_height
        self.name = window_name
        self.window = self.create_game_window()
        self.background = Color(background_rgb)
        self.drawer = Graphics(self)

    def create_game_window(self) -> pygame.surface:
        """Creates a game window that displayed the visuals of the game."""
        window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(str(self.name))
        return window

    def run(self):
        """ Runs the game window. """
        game_clock = pygame.time.Clock()
        is_running = True
        while is_running:
            game_clock.tick(self.window_fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            self.draw_background()
            self.drawer.draw_to_screen()

    def draw_background(self):
        """ Draws the screen's background. """
        self.window.fill(self.background.get_color())
        pygame.display.update()  # updates the screen


class Color:
    def __init__(self, color):  # Constructor
        """ Create a color based off of 3 values (Red, Green, Blue). """
        self.color = color  # Tuple containing Color RGB Values

    def get_color(self):  # Getter
        """ Returns the class's color upon request. """
        return self.color  # Returns the color tuple


class Text:
    def __init__(self, text: str, font_name: str, font_size: int, is_bold: bool, is_italic: bool, is_anti_alias: bool, color_rgb: tuple, x_coordinate: float, y_coordinate: float):
        self.text = text
        self.font_name = font_name
        self.font_size = font_size
        self.is_bold = is_bold
        self.is_italic = is_italic
        self.is_anti_alias = is_anti_alias
        self.color = Color(color_rgb)
        self.font = self.set_font()
        self.label = self.set_label()
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate

    def set_font(self):
        pygame.font.init()
        self.font = pygame.font.SysFont(self.font_name, self.font_size, self.is_bold, self.is_italic)
        return self.font

    def set_label(self):
        self.label = self.font.render(self.text, self.is_anti_alias, self.color.get_color())
        return self.label


class Graphics:
    def __init__(self, window):
        """ Draws a given entity onto given game window. """
        self.window = window
        self.tasks = list()

    def add_task_to_drawer(self, new_task):
        self.tasks.append(new_task)

    def draw_to_screen(self):
        """ Draws a given entity to the screen. """
        for entity in self.tasks():
            # self.window.blit(entity, )
