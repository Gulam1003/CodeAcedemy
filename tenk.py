class TankGame:
    def __init__(self, loc_x, loc_y, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        self.tank_loc_x = loc_x
        self.tank_loc_y = loc_y
        self.direction = "North"
        self.shots = {
            "North": 0,
            "East": 0,
            "South": 0,
            "West": 0
        }
        self.points = 100

    def print_map(self):
        """Print the current map of the game."""
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")
                else:
                    print(" . ", end="")
            print()

    def left(self):
        move_position = int(input(f"Enter how much you want to move left: "))
        if 0 <= self.tank_loc_x - move_position < self.N:
            self.tank_loc_x -= move_position
        else:
            print("Invalid move.")
        self.print_map()

    def right(self):
        move_position = int(input(f"Enter how much you want to move right: "))
        if 0 <= self.tank_loc_x + move_position < self.N:
            self.tank_loc_x += move_position
        else:
            print("Invalid move.")
        self.print_map()

    def downward(self):
        move_position = int(input(f"Enter how much you want to move downward: "))
        if 0 <= self.tank_loc_y + move_position < self.N:
            self.tank_loc_y += move_position
        else:
            print("Invalid move.")
        self.print_map()

    def upward(self):
        move_position = int(input(f"Enter how much you want to move upward: "))
        if 0 <= self.tank_loc_y - move_position < self.N:
            self.tank_loc_y -= move_position
        else:
            print("Invalid move.")
        self.print_map()

    def shoot(self):
        self.shots[self.direction] += 1
        hit = random.choice([True, False])  # Simulate hit or miss
        if hit:
            print("Hit!")
            self.points += 50
        else:
            print("Miss!")
            self.points -= 10

    def info(self):
        print(f"Direction: {self.direction}")
        print(f"Coordinates: ({self.tank_loc_x}, {self.tank_loc_y})")
        print(f"Total Shots: {sum(self.shots.values())}")
        for direction, shots in self.shots.items():
            print(f"Shots {direction}: {shots}")
        print(f"Points: {self.points}")


if __name__ == "__main__":
    tg = TankGame(2, 1)
    while True:
        tg.print_map()
        command = input("Input a command (left, right, upward, downward, shoot, info, quit): ").lower()
        if command == "left":
            tg.left()
        elif command == "right":
            tg.right()
        elif command == "upward":
            tg.upward()
        elif command == "downward":
            tg.downward()
        elif command == "shoot":
            tg.shoot()
        elif command == "info":
            tg.info()
        elif command == "quit":
            break
        else:
            print("Invalid command. Try again.")
