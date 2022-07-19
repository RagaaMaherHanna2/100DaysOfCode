class QuizBrain:

    def check_answer(self,question, answer):
        if answer == question.answer:
            print('Great Job')
        else:
            print('sorry')

    def ask_question(self, question):
        answer = input(question.text + "\n")
        self.check_answer(question, answer)
