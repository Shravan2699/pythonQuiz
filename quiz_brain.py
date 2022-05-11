q_no = 0
class Quizbrain:
    def __init__(self, q_data,question,ans ):
        self.q_data = q_data
        self.ques = question
        self.answer = ans

    def next_question(self):
        print(f"Q.{q_no},{quiz.ques[q_no]} (True/False): ")

