import csv

fluency_total = 0
relevance_total = 0
count = 0

with open('data/dialogue_eval.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        fluency_total += int(row['fluency_score'])
        relevance_total += int(row['relevance_score'])
        count += 1

print(f"Average fluency score: {fluency_total / count:.2f}")
print(f"Average relevance score: {relevance_total / count:.2f}")
