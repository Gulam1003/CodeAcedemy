if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # Start game loop
    while True:
        tg.print_map()
        command = input("Input a command (left, right, upward, downward, shoot, info, quit, top): ").lower()
        if command == "left":
            tg.move_West()
        elif command == "right":
            tg.move_East()
        elif command == "upward":
            tg.move_North()
        elif command == "downward":
            tg.move_South()
        elif command == "shoot":
            tg.shoot()
            if tg.points < 0:
                break
        elif command == "info":
            tg.info()
        elif command == "quit":
            tg.quit()
        elif command == "top":
            tg.display_high_scores()
        else:
            print("Invalid command. Try again.")

