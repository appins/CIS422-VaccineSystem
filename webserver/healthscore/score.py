from typing import List

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


def calculate_score(answers) -> float:
    '''
    Calculates health score of risk for covid
    The lower the score, the less risk.
    The higher the score, the higher the risk.
    '''
    score = 0.0

    #Calculate the bmi
    feet= float(answers[8])
    inches = float(answers[9])
    weight = float(answers[10])
    age = int(answers[11])

    bmi = calculate_bmi(feet, inches, weight)

    # Source used:
    # https://www.cnn.com/2021/03/15/health/bmi-covid-19-healthy-living-wellness/index.html
    #
    # Determine current score from bmi.
    # A high bmi indicates a person is
    # more likely at risk to get Covid.
    if bmi < 18.5:
        score += 5
    elif 18.5 <= bmi <= 24.9:
        score += 2.5
    elif 25 <= bmi <= 29.9:
        score += 7.5
    else:
        score += 10

    # Source used:
    # https://www.businessinsider.com/coronavirus-death-age-older-people-higher-risk-2020-2
    #
    # Determine current score from age.
    # the older a person is, the more likely
    # they are at risk of getting Covid.
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

    # Source used:
    # https://www.businessinsider.com/coronavirus-death-rates-preexisting-conditions-heart-disease-cancer-2020-2
    #
    # Determine if user has heart problems.
    # If user has heart problems, increment score by 10.
    #
    # Heart problems appears to be the highest death rate
    # for Covid, and thus, the score should be incremented
    # by 10.
    heart_prblms = int(answers[0])
    if heart_prblms:
        score += 10
    
    # Determine if user has diabetes.
    # If user has diabetes, increment score by 8.
    #
    # Diabetes appears to be the 2nd highest death rate
    # for Covid, before heart problems, and thus, 
    # the score should be incremented by 8.
    diabetes = int(answers[1])
    if diabetes:
        score += 8

    # Determine if user has lung problems.
    # If user has lung problems, increment score by 6.
    #
    # lung problems appears to be the 3rd highest death rate
    # for Covid, before heart problems and diabetes, and thus,
    # the score should be incremented by 6.
    lung_prblms = int(answers[2])
    if lung_prblms:
        score += 6

    # Determine if user has liver problems.
    # If user has liver problems, increment score by 4.
    liver_prblms = int(answers[3])
    if liver_prblms:
        score += 4
    
    # Determine if user has cancer.
    # If user has cancer, increment score by 2.
    #
    # Cancer appears to be low in death rates
    # for Covid, and thus, the score should be
    # incremented by 2.
    cancer = int(answers[4])
    if cancer:
        score += 2

    # Sources used:
    # https://www.healthline.com/health-news/covid-19-pandemic-what-we-know-about-coronavirus-reinfections#Reinfections-occur,-but-most-people-are-protected
    #
    # Determine if user tested positive for covid recently, 
    # or came into close contact with someone with covid.
    # If either one is true, decrement score by 70% of itself.
    #
    # A person who has had Covid before are likely to be immune
    # to the disease. Thus, the score should decrease.
    pos_test = int(answers[5])
    close_contact = int(answers[6])
    if pos_test or close_contact:
        score -= (score * 0.70)

    # Determine if user has experienced any symptoms of sickness.
    # if so, decrement score by 90% of itself.
    #
    # A person who is sick will likely become sicker if they 
    # got the vaccine, and thus, the score should decrease.
    symptoms = int(answers[7])
    if symptoms:
        score -= (score * 0.90)

    rounded_score = round(score, 2)
    return rounded_score
