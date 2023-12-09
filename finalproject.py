"""
    CS051P: Final Project

    Author: Liam Bayer
            and Prince Bashangezi

    Date:
"""
import matplotlib.pyplot as plt

def help_house(csvfile):
    """
    processes a CSV file and return a dictionary containing aggregated data.
    :param csvfile: (str) The path to the CSV file to be processed.
    :return: dict: A dictionary containing aggregated data based on specific columns

    """

    # Initialize an empty dictionary to store the processed data
    new_dict = {}

    # Open the CSV file for reading
    file1 = open(csvfile, "r")

    # Initialize a counter to skip the header line
    counter = 0

    # Iterate through each line in the CSV file
    for line in file1:
        # Skip the header line
        if counter != 0:
            # Preprocess the line by replacing ", " with "*"
            line = line.replace(", ", "*")

            # Split the line into a list
            lst = line.split(",")

            # Extract relevant data
            best_list = [lst[6], lst[12], lst[15]]
            tup = tuple(best_list)
            av_list = []

            # Create a key for the dictionary based on specific columns
            key = str(lst[0]) + str(lst[2]) + str(lst[7])

            # Check if the key already exists in the dictionary
            if key not in new_dict:
                # If not, add a new entry with the current tuple
                av_list.append(tup)
                new_dict[key] = av_list
            else:
                # If yes, append the current tuple to the existing entry
                new_dict[key].append(tup)

        # Increment the counter
        counter += 1

    # Close the file
    file1.close()

    # Return the final dictionary
    return new_dict

def who_won_district(d):
    """
    determines the winner for each district based on the votes.

    :param d: (dict): A dictionary where keys represent districts and values are lists of tuples
                containing candidate names and their corresponding votes.
    :return: dict: A new dictionary where keys are districts and values are the names of the winning candidates.

    """

    # Create a new dictionary to store district winners
    new_dict = {}

    # Iterate through each district in the input dictionary
    for key in d.keys():
        winner = 0  # Variable to store the maximum votes
        best = 0    # Variable to store the index of the winning candidate

        # Iterate through each candidate's votes in the current district
        for i in range(len(d[key])):
            votes = int(d[key][i][2])

            # Check if the current candidate has more votes than the current winner
            if votes > winner:
                winner = votes   # Update the winner with the new maximum votes
                best = i         # Update the index of the winning candidate

        # Store the name of the winning candidate for the current district
        new_dict[key] = d[key][best][1]

    # Return the dictionary with district winners
    return new_dict

def house_party_winner_by_state_per_year(d):
    """
    determines the party winner by state per year based on the input dictionary.
    :param d: (dict): Input dictionary where keys represent years and states, and values represent the winning party.
    :return: dict: A dictionary where keys are years and values are the winning party (DEMOCRAT, REPUBLICAN, or NONE).

    """


    party_winner = {}

    # Iterate through the input dictionary to organize data by state and year
    for key in d.keys():
        lst = []
        if key[:-3:] not in party_winner:
            lst.append(d[key])
            party_winner[key[:-3:]] = lst
        else:
            party_winner[key[:-3:]].append(d[key])

    winner_party_dict = {}

    # Iterate through the organized data to determine the winning party for each state and year
    for key1 in party_winner.keys():
        democrat = 0
        republican = 0
        for elm in party_winner[key1]:
            if elm == "REPUBLICAN":
                republican += 1
            elif elm == "DEMOCRAT":
                democrat += 1

        # Determine the winning party based on the count of Republican and Democrat votes
        if democrat > republican:
            winner_party_dict[key1] = "DEMOCRAT"
        elif republican > democrat:
            winner_party_dict[key1] = "REPUBLICAN"
        elif republican == democrat:
            winner_party_dict[key1] = "NONE"

    return winner_party_dict

def house_historical_consistency_def3(d):
    """
    analyzes historical data and groups values based on a common identifier.
    :param d: (dict): A dictionary containing historical data with keys.
    :return: dict: A dictionary where keys are derived from original keys, and values are lists of corresponding data.

    """

    consistency_dict = {}

    # Iterate through each key in the input dictionary
    for key2 in d.keys():
        lst = []

        # Extract the common identifier from the key
        identifier = key2[4:]

        # Check if the identifier is already in the consistency_dict
        if identifier not in consistency_dict:
            # If not, create a new list and add the current value
            lst.append(d[key2])
            consistency_dict[identifier] = lst
        else:
            # If it already exists, append the current value to the existing list
            consistency_dict[identifier].append(d[key2])

    return consistency_dict

def pres_historical_consistency_def3(d):
    """
     calculates historical consistency of presidential data.
    :param d: d (dict): Dictionary containing presidential data.
    :return: dict: A dictionary where keys represent years and values are lists of corresponding presidential data.

    """

    # Dictionary to store historical consistency
    consistency_dict_pres = {}

    # Iterate through the keys in the input dictionary
    for key2 in d.keys():
        lst = []

        # Extract the year from the key and use it as a simplified key for consistency_dict_pres
        year_key = key2[4:]

        # Check if the year_key is not already in consistency_dict_pres
        if year_key not in consistency_dict_pres:
            # If not, create a new list with the corresponding presidential data
            lst.append(d[key2])
            consistency_dict_pres[year_key] = lst
        else:
            # If the year_key is already present, append the presidential data to the existing list
            consistency_dict_pres[year_key].append(d[key2])

    return consistency_dict_pres

def plot_consistency_def3(d_house, d_pres):
    """
     plots a bar chart showing the consistency of voting for the House and Presidential elections in each state.
    :param d_house: (dict): Dictionary containing the voting history for the House elections in each state.
    :param d_pres: (dict): Dictionary containing the voting history for the Presidential elections in each state.
    :return: None

    """

    # Initialize variables
    state = []
    x1 = list(range(0, 50))
    y1 = []
    bar_width = 0.35

    # Calculate consistency for House elections
    for key4 in d_house.keys():
        state.append(key4[0:2])
        consistency = 0
        previous = "None"
        for i in range(len(d_house[key4])):
            if d_house[key4][i] == previous:
                consistency += int((1/24)*100)
            previous = d_house[key4][i]
        y1.append(consistency)

    # Calculate positions for Presidential elections bars
    x2 = [elem + bar_width for elem in x1]

    y2 = []
    # Calculate consistency for Presidential elections
    for key4 in d_pres.keys():
        consistency = 0
        previous = "None"
        for i in range(len(d_pres[key4])):
            if d_pres[key4][i] == previous:
                consistency += int((1/24)*100)
            previous = d_pres[key4][i]
        y2.append(consistency)

    # Plot the bar chart
    plt.bar(x1, y1, bar_width, label="House Loyalty")
    plt.bar(x2, y2, bar_width, label="Presidential Loyalty")
    plt.xticks(x1, tuple(state))

    # Set labels and title
    plt.xlabel("State Abbreviation")
    plt.ylabel("Party Consistency Percentage")
    plt.title("Consistency of State Voting for House and Presidential Elections")

    # Display legend and show the plot
    plt.legend()
    plt.show()


def help_pres(csvfile):
    """
    reads data from a CSV file and organizes it into a dictionary.
    The CSV file is assumed to have specific columns, and the function extracts
    relevant information to create a dictionary.
    :param csvfile: (str): The path to the CSV file to be processed.
    :return: dict: A dictionary where keys are a combination of two columns, and values
      are lists of tuples containing selected data from the CSV file.

    """

    # Initialize an empty dictionary to store the organized data
    new_dict = {}

    # Open the CSV file for reading
    file1 = open(csvfile, "r")

    # Initialize a counter to skip the header row
    counter = 0

    # Iterate over each line in the file
    for line in file1:
        # Skip the header row
        if counter != 0:
            # Process the line by replacing ", " with "*" and splitting it into a list
            line = line.replace(", ", "*")
            lst = line.split(",")

            # Extract specific elements from the list
            best_list = [lst[6], lst[10], lst[14]]
            tup = tuple(best_list)

            # Generate a key by combining two elements from the list
            key = str(lst[0]) + str(lst[2])

            # Check if the key is already in the dictionary
            if key not in new_dict:
                # If not, create a new entry with the key and a list containing the tuple
                new_dict[key] = [tup]
            else:
                # If the key exists, append the tuple to the existing list
                new_dict[key].append(tup)
        # Increment the counter
        counter += 1

    # Explicitly close the file
    file1.close()

    # Return the final dictionary
    return new_dict

def who_won_state_pres(election_results):
    """
     determines the winner of the presidential election in each state.
    :param election_results: (dict): A dictionary containing election results for each state.
    :return: dict: A new dictionary mapping each state to the winner of the presidential election in that state.

    """

    # Create a new dictionary to store the results
    state_winners = {}

    # Iterate through each state in the provided election results
    for state, candidates in election_results.items():
        winner_votes = 0  # Variable to track the maximum number of votes for a candidate
        winning_candidate_index = 0  # Variable to track the index of the winning candidate

        # Iterate through each candidate's votes in the current state
        for i in range(len(candidates)):
            votes = int(candidates[i][1])  # Extract the number of votes for the current candidate

            # Check if the current candidate has more votes than the current winner
            if votes > winner_votes:
                winner_votes = votes  # Update the maximum number of votes
                winning_candidate_index = i  # Update the index of the winning candidate

        # Assign the winning candidate's name to the current state in the new dictionary
        state_winners[state] = candidates[winning_candidate_index][2]

    # Return the dictionary with the winners for each state
    return state_winners


def consistency_def1(house, pres):
    """
    calculates consistency between two dictionaries. The function calculates consistency scores for each key common to
    both house and president dictionaries based on matching values. The consistency score is represented as a percentage.
    :param house: (dict): Dictionary representing data from house.
    :param pres: (dict): Dictionary representing data from president.
    :return:  dict: Consistency scores for common keys between house and president.

    """

    # Initialize an empty dictionary to store consistency scores
    consistency = {}

    # Iterate over keys in the president's dictionary
    for key in pres.keys():
        # Check if the key is also present in the house's dictionary
        if key in house.keys():
            # Extract the substring from the key, starting from the 5th character
            key_suffix = key[4:]

            # Check if the key's suffix is not already in the consistency dictionary
            if key_suffix not in consistency:
                # Initialize the consistency score for the key's suffix
                consistency[key_suffix] = 0

            # Check if the values for the key in both dictionaries match after stripping newline characters
            if house[key] == pres[key].strip("\n"):
                # Update the consistency score based on a proportional increase
                consistency[key_suffix] += int((1 / 12) * 100)

    # Return the final consistency dictionary
    return consistency


def plot_consistency_def1(d):
    """
     plots a bar chart representing party consistency percentages for each state.
    :param d: (dict): A dictionary where keys are state abbreviations and values are party consistency percentages.
    :return: None

    """

    # Generate x-axis values (0 to 49)
    x = list(range(50))
    y = []  # List to store consistency percentages
    state = []  # List to store state abbreviations
    bar_width = 0.35

    # Extract data from the dictionary and populate y and state lists
    for key in d.keys():
        y.append(d[key])
        state.append(key)

    # Plotting the bar chart
    plt.bar(x, y, bar_width)
    plt.xticks(x, tuple(state))

    # Adding labels and title to the plot
    plt.xlabel("State Abbreviation")
    plt.ylabel("Party Consistency Percentage")
    plt.title("Does State Vote the Same Party for House and President in General Elections?")

    # Display the plot
    plt.show()


def consistency_def2(house, pres):
    """
    calculates consistency between two dictionaries.
    :param house: (dict): Dictionary representing the first set of data.
    :param pres: (dict): Dictionary representing the second set of data.
    :return: dict: Consistency scores for each key in the second dictionary.

    """

    # Convert dictionaries to lists of key-value pairs
    lst1 = list(house.items())
    lst2 = list(pres.items())

    # Initialize an empty list to store inconsistent elements
    new_list = []

    # Find elements in the first list not present in the second list
    for elm in lst1:
        if elm[0] not in pres.keys():
            new_list.append(elm)

    # Initialize a dictionary to store consistency scores
    consistency = {}

    # Iterate over the first 600 elements of the second list
    for i in range(0, min(600, len(lst2))):
        # Extract the key from the second list and remove the first four characters
        key = lst2[i][0][4:]

        # If the key is not in the consistency dictionary, initialize it with a score of 0
        if key not in consistency:
            consistency[key] = 0

        # Check if the values in the second list and new_list match
        if lst2[i][1].strip("\n") == new_list[i][1]:
            # If they match, increment the consistency score for the corresponding key
            consistency[key] += int((1 / 12) * 100)

    return consistency


def plot_consistency_def2(consistency_data):
    """
    plots a bar chart to visualize the party consistency percentage of states in mid-term elections.
    :param consistency_data: (dict): A dictionary where keys are state abbreviations and values are party consistency percentages.
    :return: None

    """

    # Prepare data for plotting
    x_values = list(range(len(consistency_data)))
    loyalty_percentages = list(consistency_data.values())
    state_abbreviations = list(consistency_data.keys())

    # Set the bar width
    bar_width = 0.35

    # Create a bar chart
    plt.bar(x_values, loyalty_percentages, bar_width)

    # Set x-axis ticks and labels
    plt.xticks(x_values, tuple(state_abbreviations))

    # Set axis labels and chart title
    plt.xlabel("State Abbreviation")
    plt.ylabel("Party Consistency Percentage")
    plt.title("Party Consistency in Mid-term Elections Compared to Previous Elections")

    # Display the plot
    plt.show()


def main():
    # Get house winner data
    house_winner = house_party_winner_by_state_per_year(who_won_district(help_house("files/1976-2022-house.csv")))

    # Get presidential winner data
    pres_winner = who_won_state_pres(help_pres("files/1976-2020-president.csv"))

    # Calculate and plot consistency scores
    house_consistency = house_historical_consistency_def3(house_winner)
    pres_consistency = pres_historical_consistency_def3(pres_winner)

    plot_consistency_def1(consistency_def1(house_winner, pres_winner))
    plot_consistency_def2(consistency_def2(house_winner, pres_winner))
    plot_consistency_def3(house_consistency, pres_consistency)


if __name__ == '__main__':
    main()