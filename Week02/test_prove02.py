from prove02 import build_story


class Test_Prove02:
    def test_prove02_happy_zebra(self):
        adjective = 'happy'
        animal = 'zebra'
        verb1 = 'sneeze'
        exclamation = 'hooray'
        verb2 = 'read'
        verb3 = 'drive'
        story = build_story(adjective, animal, verb1, exclamation, verb2, verb3)

        assert story == 'The other day, I was really in trouble. It all started when I saw a very happy zebra sneeze down the hallway. ' \
                        '"Hooray!" I yelled. But all I could think to do was to read over and over. ' \
                        'Miraculously, that caused it to stop, but not before it tried to drive right in front of my family.'

    def test_prove02_tired_snail(self):
        adjective = 'tired'
        animal = 'snail'
        verb1 = 'yell'
        exclamation = 'oh no'
        verb2 = 'sing'
        verb3 = 'skip'
        story = build_story(adjective, animal, verb1, exclamation, verb2, verb3)

        assert story == 'The other day, I was really in trouble. It all started when I saw a very tired snail yell down the hallway. ' \
                        '"Oh no!" I yelled. But all I could think to do was to sing over and over. ' \
                        'Miraculously, that caused it to stop, but not before it tried to skip right in front of my family.'
        