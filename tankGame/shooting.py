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
            self.points -= 50
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