from utility import Window
from utility import Text
main_menu = Window(60, 800, 600, "testing", (255, 255, 255))
test_text = Text("Hello World!", "Century Gothic", 20, False, False, False, (100, 100, 100), 400, 300)


def game():
    main_menu.run()
    main_menu.drawer.draw_to_screen(test_text, test_text.x_coordinate, test_text.y_coordinate)



if __name__ == "__main__":
    print("Running")
    game()
