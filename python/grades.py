from numpy import *

# Each of our grades
kristen_grades = [90, 85, 100, 77, 94]
clarisse_grades = [96, 83, 89, 97, 86]
sapna_grades = [82, 91, 94, 87, 99]

# Class grade book
grade_book = [kristen_grades, clarisse_grades, sapna_grades]

'''
This is what our grade book looks like
[	[90, 85, 100, 77, 94]
	[96, 83, 89, 97, 86]
	[82, 91, 94, 87, 99] ]

'''

# Traverse through the grade book and print all the indivdual grades
for each_teacher in grade_book:
		for each_grade in each_teacher:
			print(each_grade)

# Extensions: Find the class average, median, and standard deviation
# (For the extentions google for hints!)
for each_teacher in grade_book:
	average=sum(each_teacher)/len(each_teacher)
	print(average)
#average_kristen=(sum(kristen_grades)/len(kristen_grades))
#average_clarisse=(sum(clarisse_grades)/len(clarisse_grades))
#average_sapna=(sum(sapna_grades)/len(sapna_grades))

#list_of_each_average = [average_kristen, average_clarisse,average_sapna]
#print(list_of_each_average)
class_average=(sum(list_of_each_average)/3)
print(class_average)

#total_sum=(sum[kristen_grades]+sum[clarisse_grades]+sum[sapna_grades])
#print(total_sum)

#class_average=(sum(list_of_each_average)/len(list_of_each_average))
#print(class_average)



# Super extra extensions: calculate the student with highest/lowest average
