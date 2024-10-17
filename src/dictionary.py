student_score = {'mike':90,'aron':70,'sam':60,'mark':30,'alex':25 }

hightes_score = max(student_score,key=student_score.get)
lowest_score = min(student_score,key=student_score.get)

print(hightes_score)
print(lowest_score)
student_score['ali']=75
student_score
student_score.pop('ali')
student_score