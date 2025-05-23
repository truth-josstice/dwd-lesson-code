# filter() Exercise
#
# Given a list of scores, use filter() to get a list of scores at credit level
# or better (>=70)

scores = [85, 92, 78, 60, 42, 95, 70, 53]

high_scores = filter(lambda score: score >= 70, scores)
low_scores = [x for x in scores if x < 70]

print(f'High scores: {list(high_scores)}')
print(f'Low scores: {low_scores}')
