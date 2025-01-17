def build_story(adjective, animal, verb1, exclamation, verb2, verb3):
    story = 'The other day, I was really in trouble. It all started when I saw a very {} {} {} down the hallway. ' \
            '"{}!" I yelled. But all I could think to do was to {} over and over. ' \
            'Miraculously, that caused it to stop, but not before it tried to {} right in front of my family.'

    return story.format(adjective, animal, verb1, exclamation.capitalize(), verb2, verb3)

if __name__ == '__main__':
    print('Please enter the following:\n')
    adjective = input('adjective: ')
    animal = input('animal: ')
    verb1 = input('verb: ')
    exclamation = input('exclamation: ')
    verb2 = input('verb: ')
    verb3 = input('verb: ')
    
    print(build_story(adjective, animal, verb1, exclamation.capitalize(), verb2, verb3))
