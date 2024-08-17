# Author: Avik Das
# Last Modified: August 16th, 2024

class Question:
    def __init__(
            self,
            question:str,
            fake_answers: list[str],
            correct_answer: str,
            page: int
    ):
        self.question = question
        self.fake_answers = fake_answers
        self.correct_answer = correct_answer
        self.page = page

    def get_question(self):
        return self.question
    
    def get_correct_answer(self):
        return self.correct_answer
    
    def get_fake_answers(self):
        return self.fake_answers
    
    def get_page(self):
        return self.page
    
    def set_question(self, question: str):
        self.question = question
    
    def set_fake_answers(self, fake_answers: list[str]):
        self.fake_answers = fake_answers

    def set_correct_answer(self, correct_answer: str):
        self.correct_answer = correct_answer

    def set_page(self, page: int):
        self.page = page
