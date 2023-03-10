import pygame

class GameManagement:
    def __init__(self, FPS, WindowWidth, WindowHeight, Caption):
        """ Contains the information needed for the core game loop to run."""
        self.FPS = FPS
        self.WindowWidth = WindowWidth
        self.WindowHeight = WindowHeight
        self.Caption = Caption

    def get_parameter(self, parameterType):
        """ Returns a parameter upon request. """
        if parameterType.upper() == "FPS":
            return self.FPS
        elif parameterType.upper() == "WindowWidth":
            return self.WindowWidth
        elif parameterType.upper() == "WindowHeight":
            return self.WindowHeight
        elif parameterType.upper() == "Caption":
            return self.Caption
        else:
            print("Invalid Request, Please double check spelling")
            pass

    def create_game_window(self):
        """Creates a game window that displayed the visuals of the game."""
        Window = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        pygame.display.set_caption(str(self.Caption))


Game = GameManagement(75, 800, 600, "Testing Prototype")


def GameLoop():
    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    Game.create_game_window()   # Creates Game Window

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Game Loop - code runs here
        GameClock.tick(Game.FPS)  # Runs the Game at the Desired FPS

        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False

    pygame.quit()  # Quits program


if __name__ == "__main__":  # Program Starts Here
    GameLoop()


def update(spaceship):
    # Draw a surface/sprite on the screen at the x and y coordinates provided
    WIN.blit(BACKGROUND, (0, 0))
    # Draws the Spaceship at the coordinates that the image is supposed to be according to the pygame.Rect method.
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))

    # Makes the Spaceship face the mouse. By the way, this is not my code - I adapted it from Stack Overflow
    mouseX, mouseY = pygame.mouse.get_pos()
    playerX, playerY = spaceship.centerx, spaceship.centery

    # Fancy Math Calculation that calculates the rotation required for the spaceship to face the mouse.
    angle = math.atan2(playerX - mouseX, playerY - mouseY)
    pygame.transform.rotate(SPACESHIP, angle)

    pygame.display.update()

