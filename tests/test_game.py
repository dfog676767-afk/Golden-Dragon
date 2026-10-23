import unittest

from game import GoldenDragonGame, main


class GoldenDragonGameTests(unittest.TestCase):
    def play(self, answers):
        output = []
        remaining_answers = iter(answers)
        game = GoldenDragonGame(
            input_fn=lambda _prompt: next(remaining_answers),
            output_fn=output.append,
        )
        won = game.run()
        return won, game, "\n".join(output)

    def test_rescuing_miners_allows_peaceful_victory(self):
        won, game, output = self.play(["Aurum", "2", "1", "1"])

        self.assertTrue(won)
        self.assertEqual(game.health, 2)
        self.assertIn("lets you pass", output)

    def test_resting_makes_fight_survivable(self):
        won, game, output = self.play(["Sol", "1", "2", "3"])

        self.assertTrue(won)
        self.assertEqual(game.health, 1)
        self.assertIn("outmaneuver the knight", output)

    def test_fight_without_resting_causes_retreat(self):
        won, game, output = self.play(["Sol", "2", "2", "3"])

        self.assertFalse(won)
        self.assertEqual(game.health, 0)
        self.assertIn("retreat to your mountain", output)

    def test_invalid_choice_is_reprompted(self):
        won, _, output = self.play(["", "invalid", "2", "1", "1"])

        self.assertTrue(won)
        self.assertIn("Choose one of: 1, 2.", output)

    def test_main_replays_and_exits_when_requested(self):
        answers = iter(["Aurum", "2", "1", "1", "y", "Sol", "2", "2", "2", "n"])
        output = []

        main(input_fn=lambda _prompt: next(answers), output_fn=output.append)

        self.assertEqual(output.count("THE GOLDEN DRAGON"), 2)

    def test_main_reprompts_for_invalid_replay_answer(self):
        answers = iter(["Aurum", "2", "1", "1", "maybe", "n"])
        output = []

        main(input_fn=lambda _prompt: next(answers), output_fn=output.append)

        self.assertIn("Please enter y or n.", output)


if __name__ == "__main__":
    unittest.main()
