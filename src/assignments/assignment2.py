def faculty_evaluation_result(nev, rar, som, oft, voft, alw):

    total = nev + rar + som + oft + voft + alw
    nev_perc = nev / total
    rar_perc = rar / total
    som_perc = som / total
    oft_perc = oft / total
    voft_perc = voft / total
    alw_perc = alw/total

    if alw_perc + voft_perc >= .9:
        rating = 'Excellent'
    elif oft_perc + voft_perc + alw_perc >= .8:
        rating = 'Very Good'
    elif som_perc + oft_perc + voft_ratio + alw_perc >= .7:
        rating = 'Good'
    elif rar_perc + som_perc + oft_perc + voft_perc + alw_ratio >= .6:
        rating = 'Needs Improvement'
    else:
        rating = 'Unacceptable'

    return rating
    

def get_ratings(nev,rar,som, oft,voft, alw):

    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
