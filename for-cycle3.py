school = [ 
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '7a', 'scores': [3,3,3,5,5,4]},
{'school_class': '10v', 'scores': [5,5,5,4,4,3,5]}
]
scores_number_total = 0
sum_grades_total = 0
for i in range(len(school)):
    grade = school[i]['scores']
    mean_value = sum(grade) / len(grade)
    scores_number_total += len(grade)
    sum_grades_total += sum(grade)
    mean_total = sum_grades_total / scores_number_total
    print (f"The average score of {school[i]['school_class']} is {mean_value}")
print(f"The average score in school is {mean_total}")