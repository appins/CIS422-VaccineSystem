def calculate_bmi(heightft: int, heightin: int, weight: float) -> float:
    '''
    Calculates bmi for user
    User gets asked for height in feet in inches and their weight,
    and then calculates the bmi for the user.
    '''
    height = float((heightft*12) + heightin)
    bmi = (weight / (height**2)) * 703
    rounded_bmi = round(bmi, 1)
    return rounded_bmi


def calculate_score(bmi: float, age: int, heart_prblms: bool, diabetes: bool, lung_prblms: bool, liver_prblms: bool, cancer: bool, pos_test: bool, close_contact: bool, symptoms: bool) -> float:
    '''
    Calculates health score of risk for covid
    The lower the score, the less risk.
    The higher the score, the higher the risk.
    '''
    score = 0.0

    # Determine current score from bmi.
    if bmi < 18.5:
        score += 5
    elif 18.5 <= bmi <= 24.9:
        score += 2.5
    elif 25 <= bmi <= 29.9:
        score += 7.5
    else:
        score += 10

    # Determine current score from age.
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
    elif 80 <= age <= 89:
        score += 9
    else:
        score += 10

    # Determine if user has heart problems.
    # If user has heart problems, increment score by 10.
    if heart_prblms:
        score += 10
    
    # Determine if user has diabetes.
    # if user has diabetes, increment score by 8.
    if diabetes:
        score += 8

    # Determine if user has lung problems.
    # If user has lung problems, increment score by 6.
    if lung_prblms:
        score += 6

    # Determine if user has liver problems.
    # If user has liver problems, increment score by 4.
    if liver_prblms:
        score += 4
    
    # Determine if user has cancer.
    # If user has cancer, increment score by 2.
    if cancer:
        score += 2

    # Determine if user tested positive for covid recently, 
    # or came into close contact with someone with covid.
    # If either one is true, decrement score by 70% of itself.
    if pos_test or close_contact:
        score -= (score * 0.70)

    # Determine if user has experienced any symptoms of sickness.
    # if so, decrement score by 90% of itself.
    if symptoms:
        score -= (score * 0.90)

    rounded_score = round(score, 2)
    return rounded_score
