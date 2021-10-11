# lambda functions
import entrance_score as es

absent_hours = int(input('absent hours: '))
total_hours = int(input('total hours: '))

presenceScore = es.calculatePreExamPresenceScore(absent_hours, total_hours)
print('Presence score is:', presenceScore)

isPassed = es.isPassedByPresenceScore(presenceScore)

# msg = ''
# if isPassed:
#     msg = 'Congratulations, you have passed'
# else:
#     msg = 'Sorry, you don\'t pass'

msg = 'Congratulations, you have passed' if isPassed else 'Sorry, you don\'t pass'

print(msg)





