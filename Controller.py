# Author: Avik Das
# Last Modified: August 16th, 2024

from Question import Question
from Test import Test
import re

class Controller:
    def parse_test_question(self, test_question: str):
        extract_question_pattern = re.compile(r"\d+\.\s\*\*(.+\?)\*\*\s*\(pg\.\s*(\d+)\)(.*)", flags=re.DOTALL)
        res = re.search(extract_question_pattern, test_question.strip())
        return res
    
    def parse_question_answer(self, test_question_answers: str):
        test_question_answers_arr = test_question_answers.split("\n")
        extract_question_answer_pattern = re.compile(r"-\s(\w)\) (.+)")
        matches = [re.search(extract_question_answer_pattern, answer) for answer in test_question_answers_arr]
        answer_dict = {}
        for match in matches:
            answer_dict[match.group(1)] = match.group(2)
        return answer_dict
    
    def parse_test_answers(self, test_answers: str):
        answer_list = test_answers.strip().split("\n")
        del answer_list[0]
        extract_test_answer_pattern = re.compile(r"\d+\.\s([a-zA-Z0-9])\.*")
        answer_matches = [re.search(extract_test_answer_pattern, answer) for answer in answer_list]
        return answer_matches
    
    def parse_from_file(self, filename: str):
        file = open(filename, mode="r", encoding="utf-8")
        text = file.read()
        file.close()
        questions = text.split("\n\n")
        question_matches = [self.parse_test_question(question) for question in questions[0:len(questions)-1]]
        answer_matches = self.parse_test_answers(questions[-1])
        questions = []
        for question_match, answer_match in zip(question_matches, answer_matches):
            answer_dict = self.parse_question_answer(question_match.group(3).strip())
            correct_answer = ""
            incorrect_answer = []
            for k, v in answer_dict.items():
                if(k == answer_match.group(1)):
                    correct_answer = v
                else:
                    incorrect_answer.append(v)
            
            question = Question(question_match.group(1), incorrect_answer, correct_answer, question_match.group(2))
            questions.append(question)

        test = Test(questions)
        return test
    
    def output_res(self, filename):
        test = self.parse_from_file(filename)
        f = open(filename.split(".")[0] + " RANDOMIZED.txt", mode = "w")
        randomized = test.generate_randomized_test()
        f.write(randomized)
        f.close()
        return randomized
    
def main():
    c = Controller()
    filename = input("Enter the name of the file (including the .txt): ")
    print(c.output_res(filename))
    print("\n\n")
    print("Randomized test saved in " + filename.split(".")[0] + " RANDOMIZED.txt")
        
if __name__ == '__main__':
    main()