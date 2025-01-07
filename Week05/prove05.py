message_1 = 'You are ready for your adventure ride.  Do you want to go on a GRAVEL or ROAD bike? '

message_1_1 = 'On your gravel ride, do you want to ride in the DESERT or along the BEACH? '

message_1_2 = 'On your road ride, do you want to ride in the MOUNTAINS or the CITY or the COUNTRY? '

choice1 = input(message_1).lower()

if choice1 == 'gravel':
    choice1_1 = input(message_1_1).lower()
elif choice1 == 'road':
    choice1_2 = input(message_1_2).lower()
