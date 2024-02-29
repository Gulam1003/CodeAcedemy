class TankGame:
    def __init__(self,loc_x , loc_y, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = loc_x
        self.tank_loc_y = loc_y

        direction = input('''Enter which way you want to move:
                 possible ways are:-
                 1.left
                 2.right
                 3.upward
                 4.downward''')
        if direction == "left":
            self.left()
        elif direction == "right":
            self.right()
        elif direction == "upward":
            self.upward()
        elif direction == "downward":
            self.downward()

    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")
                else:
                    print(" . ", end="")
            print()

    def left(self):
        self.tank_loc_x -= 1
        self.print_map()
        self.__init__(self.tank_loc_x,self.tank_loc_y)

    def right(self):
        self.tank_loc_x +=1
        self.print_map()
        self.__init__(self.tank_loc_x, self.tank_loc_y)

    def downward(self):
        self.tank_loc_y -= 1
        self.print_map()
        self.__init__(self.tank_loc_x, self.tank_loc_y)



    def upward(self):
        if self.tank_loc_y>
        self.tank_loc_y +1= 1
        self.__init__(self.tank_loc_x, self.tank_loc_y)

    def target_location(self,x,y):
        self.x = int(input("Enter the x-axis of target location:-"))
        self.y = int(input("Enter the y-axis of target location:-"))


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