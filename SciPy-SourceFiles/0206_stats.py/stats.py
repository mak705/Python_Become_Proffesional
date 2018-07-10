from scipy.stats import binom
import scipy as sp

n,p = 50, .25
x=sp.linspace(0,50,51)
correct_answer_points = 2
wrong_answer_points = -1
correct_answers = binom.pmf(x,n,p)
print("Probabilities for exact number of correct answers:")
print(correct_answers)
print("Sum of probabilities: ", sum(correct_answers))
print("Expected points (out of 100): ", binom.mean(n,p)*correct_answer_points)

wrong_answers = binom.pmf(x,n,1-p)
print("Probabilities for exact number of wrong answers: ")
print(wrong_answers)
print("Sum of probabilities: ", sum(wrong_answers))

expected_points=[]
for i in sp.linspace(0,50,51):
    expected_points.append(i*correct_answer_points + (50-i) * wrong_answer_points)
print("Expected points (out of 100): ", sp.mean(expected_points))