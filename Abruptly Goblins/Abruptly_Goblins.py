gamers = []

def add_gamer(gamer, gamers_list):
    if gamer["name"] and gamer["availability"]:
        gamers_list.append(gamer)

kimberly = {}
kimberly["name"] = "Kimberly Warner"
kimberly["availability"] = ["Monday", "Tuesday", "Friday"]

add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    return days

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, availability_frequency):
    for gamer in gamers_list:
        for days in gamer["availability"]:
            availability_frequency[days] += 1

calculate_availability(gamers, count_availability)
print("Days gamers are available:")
print(count_availability)
test = ""
for gamer in gamers:
    for g in gamer["name"]:
        test += g
    test += " "
#print(test)

def find_best_night(available_table):
    highest = 0
    test = ""
    for key,value in available_table.items():
        if value > highest:
            highest = value
            test = key
    return test
game_night = find_best_night(count_availability)

print("\nGamer available on first game night: " + game_night + '\n')

def available_on_night(gamers_list, day):
    people = []
    test = ""
    for gamer in gamers_list:
        for a in gamer["availability"]:
            if a == day:
                people.append(gamer["name"])
    return people
attending_game_night = available_on_night(gamers, game_night)

#print(attending_game_night)

#for gamer in gamers:
#    print(gamer['name'])

unable_to_attend_best_night = [gamer for gamer in gamers];
for i in attending_game_night:
    for gamer in gamers:
        if gamer['name'] == i:
            unable_to_attend_best_night.remove(gamer)
            
#print(unable_to_attend_best_night)


form_email = "{name} is available on {day_of_week} to play {game}."

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))
send_email(attending_game_night, game_night, "Abruptly Goblins!")


second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)

second_night = find_best_night(second_night_availability)

print("\nGamer available on second game night: " + second_night + '\n')

available_second_game_night = available_on_night(gamers, second_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins!")

print('\n')

