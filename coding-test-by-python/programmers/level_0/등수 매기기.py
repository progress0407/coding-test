from numpy import mean


def solution(scores):

    avg_scores = [mean(score) for score in scores]
    rank_scores = sorted(avg_scores, reverse=True)

    return [rank_scores.index(score) + 1 for score in avg_scores]


print(f'결과 = {solution([[80, 70], [90, 50], [40, 70], [50, 80]])}')
