class Round:

    SCORE_MAP = dict(
        # rock
        AX=4,  # rock, rock
        AY=8,  # rock, paper
        AZ=3,  # rock, scissors
        # paper
        BX=1,  # paper, rock
        BY=5,  # paper, paper
        BZ=9,  # paper, scissors
        # scissors
        CX=7,  # scissors, rock
        CY=2,  # scissors, paper
        CZ=6,  # scissors, scissors
    )

    def __init__(self, opponent_play, my_play):
        self._opponent_play = opponent_play
        self._my_play = my_play

    def opponent_play(self):
        return self._opponent_play

    def my_play(self):
        return self._my_play

    def get_score(self):
        return self.SCORE_MAP[self._opponent_play + self._my_play]


SCORE_MAP_2 = dict(
    # rock
    AX=3,  # rock, lose --> scissors
    AY=4,  # rock, draw --> rock
    AZ=8,  # rock, win  --> paper
    # paper
    BX=1,  # paper, lose --> rock
    BY=5,  # paper, draw --> paper
    BZ=9,  # paper, win  --> scissors
    # scissors
    CX=2,  # scissors, lose --> paper
    CY=6,  # scissors, draw --> scissors
    CZ=7,  # scissors, win  --> rock
)


def run_strategy(strategy_guide, score_map_override=None):
    scores = []
    for i in strategy_guide:
        opponent_play, my_play = i.split(" ")
        round = Round(opponent_play, my_play)
        if score_map_override:
            round.SCORE_MAP = score_map_override
        score = round.get_score()
        scores.append(score)
    return sum(scores)


def test_p1():
    strategy_guide = open("2022/d2.test").read().splitlines()
    sum_scores = run_strategy(strategy_guide)
    assert sum_scores == 15


def test_p1_override():
    strategy_guide = open("2022/d2.test").read().splitlines()
    sum_scores = run_strategy(strategy_guide, score_map_override=SCORE_MAP_2)
    assert sum_scores == 12


if __name__ == "__main__":
    test_p1()
    test_p1_override()
    strategy_guide = open("2022/d2.prod").read().splitlines()
    sum_scores = run_strategy(strategy_guide)
    sum_scores_override = run_strategy(
        strategy_guide=strategy_guide, score_map_override=SCORE_MAP_2
    )
    print(sum_scores, sum_scores_override)
