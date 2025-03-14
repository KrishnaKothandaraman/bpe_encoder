from collections import defaultdict


def encode_string(text):
    frequencyCounter = defaultdict(int)
    encoding_table = []
    for i in range(256):
         encoding_table.append((i, -1))


    tokens_one = []
    tokens_two = []
    for char in text:
         tokens_one.append(ord(char))

    for i in range(len(tokens_one) - 1):
        frequencyCounter[(tokens_one[i], tokens_one[i+1])]+= 1

    frequency_counter_array = [(pair, counter) for pair,counter in frequencyCounter.items()]
    max_freq_index = -1

    for i, (_, frequency) in enumerate(frequency_counter_array):
         if frequency > frequency_counter_array[max_freq_index][1]:
              max_freq_index = i
    
    if frequency_counter_array[max_freq_index][1] == 1:
         raise Exception("No more compression possible")

    encoding_table.append(frequency_counter_array[max_freq_index])

    i = 0
    while i < len(tokens_one):
         if i + 1 >= len(tokens_one):
              tokens_two.append(tokens_one[i])
              i += 1 
         else:
            if  (tokens_one[i], tokens_one[i+1]) == frequency_counter_array[max_freq_index][0]:
                tokens_two.append(len(encoding_table) - 1)
                i += 2
            else:
                tokens_two.append(tokens_one[i])
                i += 1
    return encoding_table, tokens_two