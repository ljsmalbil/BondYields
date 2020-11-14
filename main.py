



"""
Yield to maturity is similar to current yield, which divides annual cash inflows from a bond by
the market price of that bond to determine how much money one would make by buying a bond and
holding it for one year. Yet, unlike current yield, YTM accounts for the present value of a
bond's future coupon payments. In other words, it factors in the time value of money, whereas
a simple current yield calculation does not. As such, it is often considered a more thorough
means of calculating the return from a bond.
(Source: Investopedia)

"""

if __name__ == "__main__":
    face_value = 1200
    coupon_rate = 0.05
    ytm_est = 0.01

    """
    # Get the terms
    coupon_value = face_value * coupon_rate
    n = 1
    market_price = 900

    # coupon_{i} / (1 + YTM)**{n}
    YTM = 0.5

    second_term = ((1 - (1/((1 + YTM)**n)))/YTM)
    third_term = (1/(1 + YTM)**n)

    bond_price = (coupon_value * second_term) + (face_value * third_term)
    print(bond_price)

    # Get the terms
    coupon_value = face_value * coupon_rate
    n = 1
    market_price = 900

    # coupon_{i} / (1 + YTM)**{n}
    YTM = 0.5

    second_term = ((1 - (1/((1 + YTM)**n)))/YTM)
    third_term = (1/(1 + YTM)**n)
    """
    # Get the terms
    coupon_value = face_value * coupon_rate
    n = 1
    market_price = 1100

    #bond_price = (coupon_value * ((1 - (1/((1 + YTM)**n)))/YTM)) + (face_value * (1/(1 + YTM)**n))


    # Create an interval
    bond_price = 0
    YTM_pos = 0.0001
    YTM_neg = -0.0001
    print(bond_price)

    lower_bound = market_price - (market_price * 0.001)
    upper_bound = market_price + (market_price * 0.001)

    # N.B. Sensitivity is important here
    print(market_price)


    #print(lower_bound < bond_price < upper_bound)

    while (lower_bound < bond_price < upper_bound) == False:
        if face_value > market_price:
            bond_price = (coupon_value * ((1 - (1/((1 + YTM_pos)**n)))/YTM_pos)) + (face_value * (1/(1 + YTM_pos)**n))
            YTM_pos += 0.0001
            print(bond_price)
            print(YTM_pos)
        else:
            bond_price = (coupon_value * ((1 - (1 / ((1 + YTM_neg) ** n))) / YTM_neg)) + (face_value * (1 / (1 + YTM_neg) ** n))
            YTM_neg -= 0.0001
            print(bond_price)
            print(YTM_neg)

