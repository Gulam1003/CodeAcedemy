import random
class TankGame:

    def __init__(self, N: int = 7):

        self.high_scores = {}
        self.tank_direction = "North"
        self.points = 100
        self.N = N
        self.shot = 0
        self.tank_direction = "North"
        self.points = 0
        self.N = N
        self.shot = 0
        self.tank_loc_x = random.randint(0, N - 1)
        self.tank_loc_y = random.randint(0, N - 1)


        while True:
            self.target_x = random.randint(0, N - 1)
            self.target_y = random.randint(0, N - 1)
            if (self.target_x, self.target_y) != (self.tank_loc_x, self.tank_loc_y):
                break
        self.targets_shot = 0

    def print_map(self):

        tank_characters = {
            "North": " ▲ ",
            "West": " ◄ ",
            "South": " ▼ ",
            "East": " ► ",
        }

        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(tank_characters[self.tank_direction], end="")

                elif self.target_x == j and self.target_y == i:
                    print(" 0 ", end="")
                else:
                    print(" . ", end="")
            print()

    def move_North(self):
        if self.tank_loc_y > 0:
            self.tank_loc_y -= 1
            self.tank_direction = "North"

    def move_South(self):
        if self.tank_loc_y < self.N - 1:
            self.tank_loc_y += 1
            self.tank_direction = "South"

    def move_West(self):
        if self.tank_loc_x > 0:
            self.tank_loc_x -= 1
            self.tank_direction = "West"

    def move_East(self):
        if self.tank_loc_x < self.N - 1:
            self.tank_loc_x += 1
            self.tank_direction = "East"

    def display_high_scores(self):
        print("High Scores:")
        if not self.high_scores:
            print("No high scores yet.")
        else:
            for i, (name, score) in enumerate(sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True),
                                              start=1):
                print(f"{i}. {name}: {score} targets")

    def shoot(self):
        self.shot = random.randint(1, 10)
        print(self.shot)

        if self.is_facing_target():
            hit = random.choice([True, False])
            if hit:
                print("Hit!")
                self.points += 50
                self.targets_shot += 1
                # Reposition the target to a new random location
                self.target_x = random.randint(0, self.N - 1)
                self.target_y = random.randint(0, self.N - 1)
            else:
                print("Miss!")
                self.points -= 10
                if self.points < 0:
                    player_name = input("Your ammunition is ZERO. Enter your name: ")
                    self.high_scores[player_name] = self.targets_shot
                    print(f"You shot down {self.targets_shot} targets.")

                    response = input('''What you want to do now:
                    Press 'play' to play again
                    Press 'top' to view high scores
                    Press 'exit' to exit the game: ''').lower()

                    if response == 'play':
                        self.__init__(self.N)  # Reinitialize the game
                    elif response == 'top':
                        self.display_high_scores()
                    elif response == 'exit':
                        exit()


        else:
            print("You can only hit the target when facing towards target.")

    def is_facing_target(self):
        if self.tank_direction == "North" and self.tank_loc_x == self.target_x and self.tank_loc_y > self.target_y:
            return True
        elif self.tank_direction == "South" and self.tank_loc_x == self.target_x and self.tank_loc_y < self.target_y:
            return True
        elif self.tank_direction == "West" and self.tank_loc_y == self.target_y and self.tank_loc_x > self.target_x:
            return True
        elif self.tank_direction == "East" and self.tank_loc_y == self.target_y and self.tank_loc_x < self.target_x:
            return True
        else:
            return False

    def info(self):

        print(f'''tank_direction: {self.tank_direction},
tank_loc_x : {self.tank_loc_x},
tank_loc_y : {self.tank_loc_y},
points : {self.points}''')

    def quit(self):
        exit()


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
