"""Restaurant rating lister."""

def load_score(filename):
    '''list of words'''
    rest_list = open(filename)
    rest_dict = {}
    for row in rest_list:
        rest_score = row.rstrip().split(':')
        # print(repr(rest_score))
        # rest_score = rest_score.split (':')
        # print(rest_score)
        rest_dict[rest_score[0]] = rest_score[1]


    return rest_dict


rest_ratings = load_score('scores.txt')

def output_newratings (name, score):

    rest_ratings[name] = score

    tuple_rest = rest_ratings.items()

    for rest in sorted(tuple_rest):
        print(f'{rest[0]} is rated at {rest[1]}.')

    
while True:
    name_rest = input('Add restaurant name here: ')
    score_rating = input ('Score: ')

    output_newratings (name_rest, score_rating)