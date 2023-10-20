class FavoriteAnimal:
    def __init__(my, arm_length: float, leg_length: float, num_eyes: int, has_tail: bool, is_furry: bool):
        my.arm_length = arm_length
        my.leg_length = leg_length 
        my.num_eyes = num_eyes
        my.has_tail = has_tail
        my.is_furry = is_furry 

    def describe(my):
        print("My favorite animal's characteristics:")
        print(f"Arm Length: {my.arm_length} units")
        print(f"Leg Length: {my.leg_length} units")
        print(f"Number of Eyes: {my.num_eyes}")
        if my.has_tail:
            print("It has a tail.")
        else:
            print("It does not have a tail.")
        if my.is_furry:
            print("It is furry.")
        else:
            print("It is not furry.")

my_favorite_animal = FavoriteAnimal(6.0, 6.0, 2, True, True)

my_favorite_animal.describe()

# I edited this so much it was very annoying. "my" means my favorite animal which is a panda