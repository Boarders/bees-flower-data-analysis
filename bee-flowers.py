import pandas
from helpers import *

colnames =  [ 'status', 'number', 'species'
            , 'subgenus', 'family', 'subfamily'
            , 'life_history_notes', 'conversation_status', 'reference'
            , 'plant', 'link_to_plant_data', 'habitat_details'
            , 'Link to Habitat Details'
            ]

data = pandas.read_csv('bees-data.csv', names=colnames)

habitats_raw = data.plant.tolist()
habitats = list(map(lambda x : str(x), habitats_))

# Remove bad entries from habitats column with offset to avoid
# column heading.
habitats_clean = list (filter(excluded_string_test, habitats))[2:]



# split via new-lines in each entry
habitats_lines = list(map(split_lines, habitats_clean))

# Take the list of lists of species and transform it
# counting the number of occurence of each species
# and ordering via this number.
ord_flowers = transform_data(habitats_lines)
df = pandas.DataFrame(ord_flowers, columns = ['Species', 'Occurences'])
df.to_csv('flowers_ranked.csv')
