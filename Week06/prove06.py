message_1 = 'You are ready for your adventure ride.  Do you want to go on a GRAVEL or ROAD bike? '

message_1_1 = 'On your gravel ride, do you want to ride in the DESERT or along the BEACH? '
message_1_1_1 = 'On your desert ride, do you want to ride during the DAY or NIGHT? '
ending_1_1_1_1 = 'You are ready for your desert ride during the day.  Enjoy your ride!'
ending_1_1_1_2 = 'You are ready for your desert ride during the night.  Enjoy your ride!'

message_1_1_2 = 'On your beach ride, do you want to be by a LAKE or the OCEAN? '
ending_1_1_2_1 = 'You are ready for your beach ride by the lake.  Enjoy your ride!'
ending_1_1_2_2 = 'You are ready for your beach ride by the ocean.  Enjoy your ride!'

message_1_2 = 'On your road ride, do you want to ride in the MOUNTAINS or the CITY or the COUNTRY? '
message_1_2_1 = 'On your mountain ride, do you want to be in the ALPS or the PYRENEES? '
ending_1_2_1_1 = 'You are ready for your mountain ride in the Alps.  Enjoy your ride!'
ending_1_2_1_2 = 'You are ready for your mountain ride in the Pyrenees.  Enjoy your ride!'

message_1_2_2 = 'On your city ride, do you want to ride in the LONDON or PARIS? '
ending_1_2_2_1 = 'You are ready for your city ride in London.  Enjoy your ride!'
ending_1_2_2_2 = 'You are ready for your city ride in Paris.  Enjoy your ride!'

message_1_2_3 = 'On your country ride, do you want to ride in the SCOTLAND or SPAIN? '
ending_1_2_3_1 = 'You are ready for your country ride in Scotland.  Enjoy your ride!'
ending_1_2_3_2 = 'You are ready for your country ride in Spain.  Enjoy your ride!'

choice1 = input(message_1).lower()

if choice1 == 'gravel':
    choice1_1 = input(message_1_1).lower()
    if choice1_1 == 'desert':
        choice1_1_1 = input(message_1_1_1).lower()
        if choice1_1_1 == 'day':
            print(ending_1_1_1_1)
        elif choice1_1_1 == 'night':
            print(ending_1_1_1_2)
    elif choice1_1 == 'beach':
        choice1_1_2 = input(message_1_1_2).lower()
        if choice1_1_2 == 'lake':
            print(ending_1_1_2_1)
        elif choice1_1_2 == 'ocean':
            print(ending_1_1_2_2)
elif choice1 == 'road':
    choice1_2 = input(message_1_2).lower()
    if choice1_2 == 'mountains':
        choice1_2_1 = input(message_1_2_1).lower()
        if choice1_2_1 == 'alps':
            print(ending_1_2_1_1)
        elif choice1_2_1 == 'pyrenees':
            print(ending_1_2_1_2)
    elif choice1_2 == 'city':
        choice1_2_2 = input(message_1_2_2).lower()
        if choice1_2_2 == 'london':
            print(ending_1_2_2_1)
        elif choice1_2_2 == 'paris':
            print(ending_1_2_2_2)
    elif choice1_2 == 'country':
        choice1_2_3 = input(message_1_2_3).lower()
        if choice1_2_3 == 'scotland':
            print(ending_1_2_3_1)
        elif choice1_2_3 == 'spain':
            print(ending_1_2_3_2)
