from finalproject import *

def main():
    # Get house winner data
    house_winner = house_party_winner_by_state_per_year(who_won_district(help_house("files/1976-2022-house.csv")))
    # Get presidential winner data
    pres_winner = who_won_state_pres(help_pres("files/1976-2020-president.csv"))

    # Calculate and plot consistency scores
    house_consistency = house_historical_consistency_def3(house_winner)
    pres_consistency = pres_historical_consistency_def3(pres_winner)

    print("testing first definition of consistency")
    assert consistency_def1(house_winner, pres_winner)["AL"] == 67
    assert consistency_def1(house_winner,pres_winner)["OR"] == 75
    assert consistency_def1(house_winner,pres_winner)["PA"] == 42
    assert consistency_def1(house_winner, pres_winner)["AZ"] == 50
    assert consistency_def1(house_winner, pres_winner)["NV"] == 33
    print("first definition of consistency passed")

    print("testing second definition of consistency")
    assert consistency_def2(house_winner, pres_winner)["AL"] == 67
    assert consistency_def2(house_winner, pres_winner)["OR"] == 75
    #assert consistency_def2(house_winner, pres_winner)["PA"] == 50
    assert consistency_def2(house_winner, pres_winner)["AZ"] == 58
    #assert consistency_def2(house_winner, pres_winner)["NV"] == 33
    print("second definition of consistency passed")
    #
    # print("testing third definition of consistency for house")
    # assert consistency_def31(house_consistency)[] ==
    # print("third definition of consistency for house passed")
    #
    # print("testing third definition of consistency for president")
    # assert consistency_def32(pres_consistency)[] ==
    # print("third definition of consistency for president passed")



if __name__ == "__main__":
    main()
