def find_actor(birth_year):
    watch_year=int(birth_year) + 18
    actors={1973:'Roger Moore',1987:'Timothy Dalton',1995:'Pierce Brosnan',2006:'Daniel Craig'}
    for year in sorted(actors.keys(),reverse=True):
        if watch_year >= year:
            return actors[year]
birth_year=input('Please input the birth year of the person.')
print(find_actor(birth_year))

#Examples for this code
birth_year=1987
print(find_actor(birth_year))