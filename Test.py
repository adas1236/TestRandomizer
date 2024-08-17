# Author: Avik Das
# Last Modified: August 16th, 2024

import secrets

from Question import Question

class Test:
    def __init__(
            self,
            questions: list[Question]
    ):
        self.questions = questions

    def generate_randomized_test(self):
        questions_text = []
        questions_answer_key = []
        curr_question = 1
        for question in self.questions:
            correct_pos = secrets.randbelow(4)
            
            randomized_answer_arr = []
            unrandomized_fake_answers = question.get_fake_answers()
            
            while(len(unrandomized_fake_answers) > 0):
                fake = secrets.choice(unrandomized_fake_answers)
                randomized_answer_arr.append(fake)
                unrandomized_fake_answers.remove(fake)

            randomized_answer_arr.insert(correct_pos, question.get_correct_answer())

            question_text = f"{curr_question}. **{question.get_question()}** (pg. {question.get_page()})"
            for letter, choice in zip(('A', 'B', 'C', 'D'), randomized_answer_arr):
                question_text += f"\n\t- {letter}) {choice}"
            question_text += "\n\n"

            questions_text.append(question_text)
            questions_answer_key.append((correct_pos, question.get_correct_answer(), question.get_page()))
            curr_question += 1
        
        test_text = ""
        for question_text in questions_text:
            test_text += question_text
        
        test_text += "### Answer Key:\n"
        curr_question = 1
        mapper = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        for answer_id, answer_text, answer_page in questions_answer_key:
            test_text += f"{curr_question}. {mapper[answer_id]}) {answer_text} (pg. {answer_page})\n"
            curr_question += 1

        return test_text
    
# q1 = Question(
#     "What is one of the most significant aspects of EMS quality management?",
#     ["Training personnel", "Collecting data", "Equipment maintenance"],
#     "Continuous improvement",
#     3
# )
# t1 = Test([q1])
# print(t1.generate_randomized_test())