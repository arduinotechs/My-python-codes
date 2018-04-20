class Enemy:
    life = 3

    def attack(self):
        self.life -= 1
        print("Hey Don't hurt me")

    def check_life(self):
        if self.life <= 0:
            print("You killed me!")
        else:
            print(str(self.life) + " HP remains")


enemy1 = Enemy()
enemy2 = Enemy()

enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy2.check_life()