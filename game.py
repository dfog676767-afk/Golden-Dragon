"""A small, choice-driven adventure about a golden dragon."""


class GoldenDragonGame:
    def __init__(self, input_fn=input, output_fn=print):
        self.input = input_fn
        self.output = output_fn
        self.health = 2
        self.max_health = 3
        self.treasure = 0
        self.kindness = 0
        self.name = "Aurum"

    def _choose(self, prompt, choices):
        self.output(prompt)
        for key, description in choices.items():
            self.output(f"  {key}. {description}")

        while True:
            answer = self.input("> ").strip()
            if answer in choices:
                return answer
            self.output(f"Choose one of: {', '.join(choices)}.")

    def run(self):
        self.output("THE GOLDEN DRAGON")
        self.output("You are a young dragon setting out from your mountain home.")
        dragon_name = self.input("What is your dragon's name? ").strip()
        if dragon_name:
            self.name = dragon_name
        self.output(f"\nYour adventure begins, {self.name}. You have {self.health} health.")

        mountain_choice = self._choose(
            "\nAt the mountain pass, a quiet alcove offers shelter.",
            {
                "1": "Rest and recover 1 health.",
                "2": "Search the rocks for a forgotten coin.",
            },
        )
        if mountain_choice == "1":
            self.health = min(self.max_health, self.health + 1)
            self.output(f"You rest by a warm spring. Health: {self.health}.")
        else:
            self.treasure += 1
            self.output("You uncover a bright gold coin. Treasure: 1.")

        village_choice = self._choose(
            "\nSmoke rises from a village mill. Miners are trapped inside.",
            {
                "1": "Rescue the miners with a careful breath of warm air.",
                "2": "Demand a reward instead of helping.",
            },
        )
        if village_choice == "1":
            self.kindness += 1
            self.output("The miners are safe, and the villagers cheer your name.")
        else:
            self.treasure += 2
            self.output("The villagers hand over two coins so you will leave them alone.")
            self.output("Treasure: 2.")

        final_choice = self._choose(
            "\nAt the old bridge, a knight guards the way to a legendary hoard.",
            {
                "1": "Ask the knight to trust the good you have done.",
                "2": "Offer 2 coins to pass.",
                "3": "Challenge the knight to a fight.",
            },
        )
        if final_choice == "1" and self.kindness:
            self.output(
                f"\nThe knight has heard of your kindness, {self.name}, and lets you pass."
            )
            self.output("You reach the hoard and become the Golden Dragon of legend!")
            return True
        if final_choice == "2" and self.treasure >= 2:
            self.treasure -= 2
            self.output("\nThe knight accepts your offering and steps aside.")
            self.output("You reach the hoard and become the Golden Dragon of legend!")
            return True

        if final_choice == "1":
            self.output("\nThe knight has not heard of your good deeds and raises a shield.")
        elif final_choice == "2":
            self.output("\nYou do not have enough coins. The knight raises a shield.")
        else:
            self.output("\nThe knight accepts your challenge!")

        self.health -= 2
        if self.health <= 0:
            self.output("The battle is too much. You retreat to your mountain to recover.")
            return False

        self.output(f"You outmaneuver the knight! Health remaining: {self.health}.")
        self.output("You reach the hoard and become the Golden Dragon of legend!")
        return True


def main(input_fn=input, output_fn=print):
    while True:
        GoldenDragonGame(input_fn=input_fn, output_fn=output_fn).run()
        while True:
            answer = input_fn("\nPlay again? (y/n) ").strip().lower()
            if answer in ("y", "yes"):
                break
            if answer in ("n", "no"):
                return
            output_fn("Please enter y or n.")


if __name__ == "__main__":
    main()
