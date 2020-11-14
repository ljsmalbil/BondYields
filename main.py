from yield_measures import YieldMeasures

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
    coupon_rate = 0.05
    market_price = 1000
    face_value = 1200

    bond = YieldMeasures(face_value=face_value, market_price=market_price, coupon_rate=coupon_rate)
    print(bond.current_yield())

    print('\n')

    YTM = bond.yield_to_maturity(n=12)

    if YTM > coupon_rate:
        print('Because the coupon rate is higher than the YTM, the bond trades at a premium.\n')
        print(YTM)
    else:
        print('Because the coupon rate is lower than the YTM, the bond trades at a discount.\n')
        print(YTM)