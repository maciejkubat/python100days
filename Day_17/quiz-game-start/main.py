from question_model import Question
from quiz_brain import QuizBrain
import requests

def get_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def create_question_bank(data):
    question_bnk = []
    for question in data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bnk.append(new_question)
    return question_bnk

def main():
    api_url = "https://opentdb.com/api.php?amount=12&type=boolean"
    question_json = get_json_from_api(api_url)
    question_data = (question_json["results"])
    question_bank = create_question_bank(question_data)
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You completed the quiz")
    print(f"Your final score was {quiz.score}/{len(question_bank)}")