import tkinter as tk
import random

class UFOGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UFO vs. Humans")
        self.ufo_health = 1000
        self.num_humans = random.randint(1, 5)
        self.human_health = [100] * self.num_humans

        self.label = tk.Label(self.root, text="UFO vs. Humans")
        self.label.pack()

        self.attack_button = tk.Button(self.root, text="Attack", command=self.attack)
        self.attack_button.pack()

    def attack(self):
        attacker = random.choice(["UFO", "Human"])
        if attacker == "UFO":
            target = random.randint(0, self.num_humans - 1)
            damage = random.randint(1, 50)
            self.human_health[target] -= damage
            message = f"UFO attacked Human {target + 1} for {damage} damage."
        else:
            damage = random.randint(1, 100)
            self.ufo_health -= damage
            message = f"Human attacked UFO for {damage} damage."

        if self.ufo_health <= 0 or all(hp <= 0 for hp in self.human_health):
            if self.ufo_health <= 0:
                message += "\nUFO has been defeated! Humans win!"
            else:
                message += "\nAll humans have been defeated! UFO wins!"
            self.attack_button.config(state=tk.DISABLED)

        self.label.config(text=message)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = UFOGame()
    game.run()
