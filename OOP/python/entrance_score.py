
def calculatePreExamPresenceScore(absent_hours: int, total_hours: int) -> float:
    a = 1 - (absent_hours / total_hours)
    return round(a * 10)

def isPassedByPresenceScore(presence_score: float) -> bool:
    return presence_score > 7