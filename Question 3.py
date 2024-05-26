import csv
with open('a.txt', 'r') as file:
    lines = file.readlines()
    questions = [line.strip().split(':')[0] for line in lines]
    answers = [line.strip().split(':')[1] for line in lines]
user_name = input("Enter your name: ")
score = 0
for i, question in enumerate(questions):
    user_answer = input(f"{question} ").lower()
    if user_answer == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {answers[i]}.")
percentage_score = (score / 20) * 100
print(f"\nYour score: {score}/20 ({percentage_score:.2f}%)")
with open('quiz_results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([user_name, percentage_score])
