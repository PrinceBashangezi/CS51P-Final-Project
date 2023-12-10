from finalproject import *


def main():
    """
    The main function that does testing of election consistency.
    """
    # Get house winner data
    house_winner = house_party_winner_by_state_per_year(who_won_district(help_house("files/1976-2022-house.csv")))

    # Get presidential winner data
    pres_winner = who_won_state_pres(help_pres("files/1976-2020-president.csv"))

    # Calculate consistency scores
    house_consistency = house_historical_consistency_def3(house_winner)
    pres_consistency = pres_historical_consistency_def3(pres_winner)

    # Testing the first definition of consistency
    print("Testing first definition of consistency")
    assert consistency_def1(house_winner, pres_winner)["AL"] == 67
    assert consistency_def1(house_winner, pres_winner)["OR"] == 75
    assert consistency_def1(house_winner, pres_winner)["PA"] == 42
    assert consistency_def1(house_winner, pres_winner)["AZ"] == 50
    assert consistency_def1(house_winner, pres_winner)["NV"] == 33
    print("First definition of consistency passed")

    # Testing the second definition of consistency
    print("Testing second definition of consistency")
    assert consistency_def2(house_winner, pres_winner)["AL"] == 67
    assert consistency_def2(house_winner, pres_winner)["OR"] == 75
    assert consistency_def2(house_winner, pres_winner)["PA"] == 50
    assert consistency_def2(house_winner, pres_winner)["AZ"] == 58
    assert consistency_def2(house_winner, pres_winner)["NV"] == 33
    print("Second definition of consistency passed")

    # Testing the third definition of consistency for the House
    print("Testing third definition of consistency for the House")
    assert consistency_def31(house_consistency)["AL"] == 96
    assert consistency_def31(house_consistency)["OR"] == 100
    assert consistency_def31(house_consistency)["PA"] == 61
    assert consistency_def31(house_consistency)["AZ"] == 57
    assert consistency_def31(house_consistency)["NV"] == 61
    print("Third definition of consistency for the House passed")

    # Testing the third definition of consistency for the President
    print("Testing third definition of consistency for the President")
    assert consistency_def32(pres_consistency)["AL"] == 91
    assert consistency_def32(pres_consistency)["OR"] == 91
    assert consistency_def32(pres_consistency)["PA"] == 64
    assert consistency_def32(pres_consistency)["AZ"] == 73
    assert consistency_def32(pres_consistency)["NV"] == 73
    print("Third definition of consistency for the President passed")


if __name__ == "__main__":
    main()