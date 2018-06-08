envs = ['bus', 'cafe/restaurant', 'car', 'city_center', 'forest_path',  'grocery_store', 'home', 
       'beach', 'library', 'metro_station', 'office', 'residential_area', 'train', 'tram', 'park']

def labels_to_numeric(labels, decode=True):
    '''Convert a list of TUT Acoustic Scenes 2017 environment labels to zero-based indexes.'''
    if decode:
        labels = [l.decode() for l in labels]
    return [envs.index(l) for l in labels]

def numeric_to_labels(class_indexes):
    '''Convert a list of zero-based indexes to TUT Acoustic Scenes 2017 environment labels.'''
    return [envs[ind] for ind in class_indexes]