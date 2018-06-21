# Hidden Markov Model

In this problem, we assume that the weather is a markov process governed by the following transition probabilities:

|  | Rainy | Sunny |
|:---: | :---:  | :---:  |
|**Rainy** | 0.5  | 0.5  |
|**Sunny** | 0.2  | 0.8  |


Furthermore, we cannot observe the weather directly, instead we can only observe whether or not our neighbor carries an umbrella on any given day.

The goal of the program is to determine the most likely sequence of weather events given the umbrella observations.

   