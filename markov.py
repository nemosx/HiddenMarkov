RAINY = 0
SUNNY = 1

states = (RAINY, SUNNY)

# We observe the umbrella on days 1, 2, 4, and 5
umbrella_observations = (1, 2, 4, 5)

# P(NO UMBRELLA | RAIN), P(NO UMBRELLA | SUNNY)
# P(UMBRELLA | RAIN), P(UMBRELLA | SUNNY)
observation_probabilities = ((0.1, 0.8),
                             (0.9, 0.2))

# P(R -> R), P(R -> S)
# P(S -> R), P(S -> S)
transition_matrix = ((0.5, 0.5),
                     (0.2, 0.8))

most_likely = [[None for y in range(2)] for x in range(6)]
most_likely_states = [[None for y in range(2)] for x in range(6)]

# We assume Sunday has a 50/50 chance for RAINY/SUNNY
most_likely[0] = [0.5, 0.5]

for current_day in range(1, 6):
    observed_umbrella = 0;
    if current_day in umbrella_observations:
        observed_umbrella = 1
    for state in states:
        max_likely = -1
        max_likely_state = None
        for previous_state in states:
            likelihood = most_likely[current_day - 1][previous_state] * transition_matrix[previous_state][state] * \
                         observation_probabilities[observed_umbrella][state]

            if likelihood > max_likely:
                max_likely = likelihood
                max_likely_state = previous_state

        most_likely[current_day][state] = max_likely
        most_likely_states[current_day][state] = max_likely_state

def weather_text_from_state(state):
    return "RAINY" if state == 0 else "SUNNY"

def print_most_likely_sequence(day_number, most_probable_prev_state):
    if day_number is -1:
        return
    print_most_likely_sequence(day_number - 1, most_likely_states[day_number][most_probable_prev_state])
    print("Day#", day_number, weather_text_from_state(most_probable_prev_state))


day_5_weather = SUNNY
if most_likely[5][RAINY] > most_likely[5][SUNNY]:
    day_5_weather = RAINY

print_most_likely_sequence(5, day_5_weather)


