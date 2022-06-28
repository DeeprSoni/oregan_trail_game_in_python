
print("This game is programmed by Deep Soni")                                                                                   #Introduction
print("Backstory - You have come to USA from Ireland to escape the potato famine, and you are now looking for your uncle")
print("in California to work with him in the gold mines. So you took a boat and reached USA, and now you are in the middle")
print("of nowhere. To play the game you have to choose one of two options (Remember - first option is 0 and second option is 1). You final goal is to reach California, restart the game if you choose wrong options.")

print()
print()

left_or_right = input("Do you want to go left or right? (Left = 0, Right = 1): ")
if left_or_right == "0":
    cross_river_or_wait = input("There is a river, so do you want to cross it now or wait for night? (Cross now = 0, Wait for night = 1): ")
    if cross_river_or_wait == "0":
        walk_or_cattle = input("Now, do you want to walk or ride a cattle? (Walk = 0, cattle = 1): ")
        if walk_or_cattle == "0":
            stay_in_village_or_leave = input("Now you have reached a village, so do you want to stay here or leave the village? (Stay in village = 0, leave the village = 1: ")
            if stay_in_village_or_leave == "0":
                print("You have been killed by the villagers, play the game again and choose different options next time!")
            elif stay_in_village_or_leave == "1":
                print("You have now reached oregon, play the game again and choose different options next time!")
            else :
                print("Please enter either 1 or 0")
        elif walk_or_cattle == "1":
            print("Your cattles went out of control and you are lost, play the game again and choose different options next time!")
        else :
            print("Please enter either 0 or 1")
    elif cross_river_or_wait == "1":
        stay_or_dont_stay_in_hotel = input("Do you want to stay in hotel or don't stay in hotel? (Stay = 0, don't stay = 1): ")
        if stay_or_dont_stay_in_hotel == "0":
            order_or_not_order_food = input("Do you want to order food or not? (Order food = 0, not order food = 1): ")
            if order_or_not_order_food == "0":
                print("You were poisoned by the food and you died. play the game again and choose different options next time!")
            elif order_or_not_order_food == "1":
                accompany_or_not = input("A stranger asks you if he could accompany you to reach California, do you want to go with him? (Yes = 0, No = 1): ")
                if accompany_or_not == "0":
                    print("You have reached Mexico, play the game again and choose different options next time!")
                elif accompany_or_not == "1" :
                    print("The stranger kills you. play the game again and choose different options next time!")
                else :
                    print("Please enter either 0 or 1")
            else :
                print("Please enter either 0 or 1")
        elif stay_or_dont_stay_in_hotel == "1" :
            light_fire_or_not = input("It is night now, do you want to light fire? (Yes = 0, No = 1): ")
            if light_fire_or_not == "0":
                print("You have burned yourself. play the game again and choose different options next time!")
            elif light_fire_or_not == "1":
                cross_river_now = input("Do you want to cross river now? (Yes = 0, No = 1): ")
                if cross_river_now == "0":
                    print("You have reached Nevada. play the game again and choose different options next time!")
                elif cross_river_now == "1":
                    print("You have died of thirst now. play the game again and choose different options next time!")
                else :
                    print("Please enter either 0 or 1")
            else :
                print("please enter either 0 or 1")
        else :
            print("please enter either 0 or 1")
    else :
        print("Please enter either 0 or 1")
elif left_or_right == "1":
    ask_locals_or_not = input("Do you want to ask a local about California? (Yes = 0, No = 1): ")
    if ask_locals_or_not == "0":
        going_with_merchants_or_not = input("After you ask the local, he shows that merchants are also going to California, do you want to go with them? (Yes = 0, No = 1): ")
        if going_with_merchants_or_not == "0":
            play_cards_with_merchants = input("The merchants are playing cards, do you want to play with them? (Yes = 0, No = 1): ")
            if play_cards_with_merchants == "0":
                print("They lose the game, and in rage they kill you. play the game again and choose different options next time!")
            elif play_cards_with_merchants == "1":
                ask_merchants = input("Do you want to ask them where they are going? (Yes = 0, No = 1): ")
                if ask_merchants == "0":
                    take_riches_and_run = input("Do you take their riches and run? (Yes = 0, No = 1): ")
                    if take_riches_and_run == "0":
                        print("You reach Canada. play the game again and choose different options next time!")
                    elif take_riches_and_run == "1":
                        print("Congratulations, you have reached California!")
                    else:
                        print("Please enter either 0 or 1")
                elif ask_merchants == "1":
                    print("You reach Wyoming. play the game again and choose different options next time!")
                else :
                    print("Please enter either 0 or 1")
            else :
                print("Please enter either 0 or 1")
        elif going_with_merchants_or_not == "1":
            hiring_a_horse_or_not = input("Do you want to hire a horse now? (Yes = 0, No = 1): ")
            if hiring_a_horse_or_not == "0":
                print("You have reached Texas. play the game again and choose different options next time!")
            elif hiring_a_horse_or_not == "1":
                walk_through_desert_or_not = input("Do you want to walk through desert or not? (Yes = 0, No = 1): ")
                if walk_through_desert_or_not == "0":
                    print("You have reached Utah. play the game again and choose different options next time!")
                elif walk_through_desert_or_not == "1":
                    print("You have starved to death. play the game again and choose different options next time!")
                else :
                    print("Please enter either 0 or 1")
            else :
                print("Please enter either 0 or 1")
        else :
            print("Please enter either 0 or 1")
    elif ask_locals_or_not == "1":
        roam_around_or_stay = input("Do you want to roam around or stay? (Roam around = 0, Stay at one place = 1): ")
        if roam_around_or_stay == "0":
            print("You almost reached California, but died of hunger on the way. play the game again and choose different options next time!")
        elif roam_around_or_stay == "1":
            wait_for_uncle_to_come = input("Do you want to wait for your uncle to come and pick you up? (Yes = 0, No = 1): ")
            if wait_for_uncle_to_come == "0":
                print("You are killed by mobsters. play the game again and choose different options next time!")
            elif wait_for_uncle_to_come == "1":
                print("You die of hunger. play the game again and choose different options next time!")
            else :
                print("Please enter either 0 or 1")
        else :
            print("Please enter either 0 or 1")
    else :
        print("Please enter either 0 or 1")
else :
    print("Please enter either 0 or 1")
