import random


class TankGame:

    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
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

        # Ensure that the target is not initially placed at the tank's position
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


        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(tank_characters[self.tank_direction], end="")

                elif self.target_x == j  and self.target_y == i:
                    print(" 0 ", end="")
                else:
                    print(" . ", end="")
            print()



    def display_high_scores(self):
        print("High Scores:")
        if not self.high_scores:
            print("No high scores yet.")
        else:
            for i, (name, score) in enumerate(sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True), start=1):
                print(f"{i}. {name}: {score} targets")






    def info(self):

        print(f'''tank_direction: {self.tank_direction},
tank_loc_x : {self.tank_loc_x},
tank_loc_y : {self.tank_loc_y},
points : {self.points}''')


    def quit(self):
        exit()



