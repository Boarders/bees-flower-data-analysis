import re
from collections import OrderedDict
from collections import Counter

# split a string into a list of its lines
def split_lines(h):    
    return h.splitlines()

# function to decide if a string is in a set of strings
def is_not_excluded (str, strings):
    return str not in strings

# set of non-species strings in our data
excluded_strings = { 'nan'
                   , '--'
                   , 'Sheffield et al. 2011a'
                   , 'Sheffield et al. 2011b'
                   , 'Bartomeus et al. 2013'
                   , 'Ascher & Pickering 2012'
                   , 'Ascher & Pickering 2012'
                   , '???'
                   , ' introduced from Eurasia'
                   , 'Mangum and Brooks 1997, Mangum and Sumner 2003, Maier 2009, Sheffield et al. 2011a'
                   }

# test whether our string is in excluded data set
excluded_string_test = lambda str : is_not_excluded(str, excluded_strings)  

# split species into the name and the data after @
def split_species(s):
    return s.split("@")

# split each of the species in our data
def split_all(ls):
    return list(map(split_species, ls))

# sum the integers in a list
def sum_ints(ls):
    acc = 0
    for l in ls:
        i = int(l)
        acc += i
    return acc

# get the integers from the species metadata
def get_int(s):
    regex_ints = r'\((\d+)\)+'
    nums = re.findall(regex_ints, s)
    return sum_ints(nums)

# return the integers in the species metadata or 1 if
# it is not present
def get_ints_pair(p):
    if (len(p) == 1):
        return (p[0],1)
    else:
        return (p[0], get_int(p[1]))

# get the species and number of occurences for each species entry
def organise_flower(lp):
    return list(map(get_ints_pair, lp))

# get the species and number of occurence over all species
def organise_flowers(lp):
    return list(map(organise_flower,lp))

# create a dictionary of flower species along with its number of occurences
def count_data(ls):
    keys = list(map(lambda p: p[0], ls))
    dict = OrderedDict.fromkeys(keys, 0)
    for val, weight in ls:
        dict[val] += weight
    return dict

# merge all the dictionaries of flower species for each bee
def count_all_data(lss):
    counter = Counter ()
    for ls in lss:
        dict = count_data(ls)
        counter.update(dict)
    return counter

# tranform the entire data set using the above functions.
def transform_data(hs):
    h1 = list(map(split_all, hs))
    h2 = organise_flowers(h1)
    h3 = count_all_data(h2)
    ord_data  = sorted(h3.items(), key = lambda p : p[1], reverse = True)
    return ord_data




