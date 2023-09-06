import argparse

from Bowling import BowlingResult

parser = argparse.ArgumentParser()
parser.add_argument('--result', required=True, help='Результаты фрейма для подсчёта очков')
args = parser.parse_args()

bowlresult = BowlingResult(game_result=args.result)
print(f'Количество очков: {bowlresult.get_score()}')
