def calculate_score(age: int, bmi: float, diabetes: bool, heart_prblms: bool, lung_prblms: bool, liver_prblms: bool, cancer: bool, pos_test: bool, close_contact: bool, symptoms: bool) -> float:
    '''
    Calculates health score of risk for covid
    The lower the score, the less risk.
    The higher the score, the higher the risk.
    '''
    score = 0.0

    # determine current score from age
    if 0 <= age <= 9:
        score += 1
    elif 10 <= age <= 19:
        score += 2
    elif 20 <= age <= 29:
        score += 3
    elif 30 <= age <= 39:
        score += 4
    elif 40 <= age <= 49:
        score += 5
    elif 50 <= age <= 59:
        score += 6
    elif 60 <= age <= 69:
        score += 7
    elif 70 <= age <= 79:
        score += 8
    else:
        score += 9

    # determine current score from bmi
    if bmi < 18.5:
        score += 2
    elif 18.5 <= bmi <= 24.9:
        score += 1
    elif 25 <= bmi <= 29.9:
        score += 3
    elif 30 <= bmi <= 34.9:
        score += 4
    else:
        score += 5

    # determine if user has diabetes
    # if user has diabetes, increment score by 4
    if diabetes:
        score += 4
    
    # determine if user has heart problems
    # if user has heart problems, increment score by 5
    if heart_prblms:
        score += 5

    # determine if user has lung problems
    # if user has lung problems, increment score by 6
    if lung_prblms:
        score += 6

    # determine if user has lung problems
    # if user has lung problems, increment score by 7
    if liver_prblms:
        score += 7
    
    # determine if user has lung problems
    # if user has lung problems, increment score by 8
    if cancer:
        score += 8

    # determine if user tested positive for covid recently
    # if user has tested positive, increment score by 9
    if pos_test:
        score += 9

    # determine if use has came into close contact with someone with covid
    # if true, increment score by 10
    if close_contact:
        score += 10

    # determine if user has experienced any symptoms of sickness
    # if so, increment score by 11
    if symptoms:
        score += 11

    return score
