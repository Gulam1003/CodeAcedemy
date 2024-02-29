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

            elif self.target_x == j and self.target_y == i:
                print(" 0 ", end="")
            else:
                print(" . ", end="")
        print()
