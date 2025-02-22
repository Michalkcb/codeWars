def human_years_cat_years_dog_years(human_years):
    # Your code here
    #human years
    h = human_years
    #cat & dog years
    if (human_years == 1):
        c=15
        d=15
    if (human_years == 2):
        c = 15 + 9
        d = 15+9
    if (human_years > 2):
        c = 15 + 9 + (human_years -2)*4
        d = 15 + 9 + (human_years -2)*5
    return [h,c,d]
