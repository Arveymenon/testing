class Question:


    def __init__(self, section_id, question):
        self.section_id = section_id
        self.question = question
        self.test = 123

    def printing(self, new_id):
        print(self.question)
        print(self.test + self.section_id)
        print(self.section_id)

def main():
    
    # Create question
    question = Question(section_id=1, question='TESTING')
    question.question = "new question"
    question.section_id = 1
    
    question.printing('123')

if __name__ == "__main__":
    main()
    pass