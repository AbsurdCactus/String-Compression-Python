def string_compresser(given_string):

    # This is a brute force solution. Try writing more efficient code 
    # the next time you revisit this. But good job!
    compressed_string = ""
    consecutive_counter = 0

    for i in range(len(given_string)):

        consecutive_counter += 1

        if i + 1 >= len(given_string) or given_string[i] != given_string[i+1]: 
            compressed_string += "" + given_string[i] + str(consecutive_counter)
            consecutive_counter = 0

    
    if len(compressed_string) == len(given_string):
        return given_string
    return compressed_string



 



