# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville',
         'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie',
         'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo',
         'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma',
         'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September',
          'September', 'September', 'September', 'September', 'September', 'October',
          'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September',
          'July', 'August', 'September', 'October', 'August', 'September', 'October',
          'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961,
         1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004,
         2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160,
                       160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165,
                       160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas',
                      'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands',
                      'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
                  ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia',
                      'The Carolinas', 'Virginia'],
                  ['Southeastern United States',
                      'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'],
                  ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'],
                  ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'],
                  ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America',
                      'Mexico', 'United States Gulf Coast'],
                  ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas',
                      'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
                  ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'],
                  ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia',
                      'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands',
                      'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico',
                      'Dominican Republic', 'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M',
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M',
           '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B',
           '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B',
           '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107,
          65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:


def damage_converted(damages):
    damages_new = []
    conversion = {"M": 1000000, "B": 100000000}
    for i in damages:
        if i == "Damages not recorded":
            damages_new.append(i)
        elif not i.find("M") != -1:
            j = float(i[0:i.find("M")]) * conversion["M"]
            damages_new.append(j)
        elif i.find("B") != -1:
            k = float(i[0:i.find("B")]) * conversion["B"]
            damages_new.append(k)
    return damages_new


new_damages = damage_converted(damages)


def dictionary(name, month, year, max_sustained_winds, areas_affected, new_damages, death):
    hurricanes_info = {}
    length = len(name)
    for i in range(length):
        hurricanes_info[name[i]] = {
            "names": name[i],
            "month": month[i],
            "year": year[i],
            "max sustained winds": max_sustained_winds[i],
            "areas affected": areas_affected[i],
            "damage": new_damages[i],
            "death": death[i]
        }
    return hurricanes_info


dict_hurricane = dictionary(
    names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
print(dict_hurricane)

""" """


def hurricane_by_year(hurricanes_info):
    hurricane_year = {}
    for i in hurricanes_info:
        current_year = hurricanes_info[i]["year"]
        current_hurricane = hurricanes_info[i]
        if current_year not in hurricane_year:
            hurricane_year[current_year] = current_hurricane
    return hurricane_year


 print(hurricane_by_year(dict_hurricane))


# write your count affected areas function here:

def affect_areas_dict(hurricane_info):
    affected_dict = {}
    for i in hurricane_info:
        for area in hurricane_info[i]["areas affected"]:
            if area not in affected_dict:
                affected_dict[area] = 1
            else:
                affected_dict[area] += 1
    return affected_dict


affected_area_all = affect_areas_dict(dict_hurricane)
 print(affected_area_all)


# write your find most affected area function here:

def most_affected(affected_areas):
    most_affected_dict = dict(
        sorted(affected_areas.items(), key=lambda item: item[1], reverse=True))
    return most_affected_dict


 print(most_affected(affected_area_all))


# write your greatest number of deaths function here:

def deaths_by_hurricane(hurricane_info):
    deaths_dict = {}
    for i in hurricane_info:
        name_of_hurricane = hurricane_info[i]["names"]
        deaths_from_hurricane = hurricane_info[i]["death"]
        deaths_dict[name_of_hurricane] = deaths_from_hurricane
        sorted_deaths = dict(
            sorted(deaths_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_deaths


print(deaths_by_hurricane(dict_hurricane))


# write your catgeorize by mortality function here:
def categorization_by_mortality(hurricane_info):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in hurricane_info:
        num_deaths = hurricane_info[i]["death"]
        if num_deaths == mortality_scale[0]:
            hurricane_mortality[0].append(hurricane_info[i])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricane_mortality[1].append(hurricane_info[i])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricane_mortality[2].append(hurricane_info[i])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricane_mortality[3].append(hurricane_info[i])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricane_mortality[4].append(hurricane_info[i])
        elif num_deaths > mortality_scale[4]:
            hurricane_mortality[5].append(hurricane_info[i])
    return hurricane_mortality


 print(categorization_by_mortality(dict_hurricane))
# write your greatest damage function here:


def greatest_damage(hurricane_info):
    great_damage = 0
    name_of_hurricane = ""
    for i in hurricane_info:
        if hurricane_info[i]["damage"] == "Damages not recorded":
            pass
        elif hurricane_info[i]["damage"] > great_damage:
            great_damage = hurricane_info[i]["damages"]
            name_of_hurricane = hurricane_info[i]
    return great_damage.name_of_hurricane



# write your catgeorize by damage function here """

def categorize_by_damage(hurricanes):
  damage_scale = {0: 0,1: 100000000,2: 1000000000,3: 10000000000,4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    total_damage = hurricanes[cane]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage
