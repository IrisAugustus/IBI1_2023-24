class students:
    def __init__(self, name, major, portfolio_score, group_score, exam_score):
        self.name= name
        if major not in ["BMS", "BMI"]:
            raise ValueError("Major must be either 'BMS' or 'BMI'")
        self.major= major
        self._validate_score(portfolio_score)
        self._validate_score(group_score)
        self._validate_score(exam_score)
        self.portfolio_score= portfolio_score
        self.group_score= group_score
        self.exam_score= exam_score
    def _validate_score(self, score):
        if not 0<=score<=100:
            raise ValueError('The scores are out of 100! Check the input.')
    def __str__(self):
        return f'Name:{self.name}, Major:{self.major}, Portfolio_score:{self.portfolio_score}, Group_score:{self.group_score}, Exam_score:{self.exam_score}'
    
#Examples for the class
student1 = students("Alice", "BMI", 90, 85, 95)
student2 = students("Bob", "BMS", 85, 90, 88)
student3 = students('Cindy', 'BMS', 100, 105, 90)
print(student1)
print(student2)
print(student3)