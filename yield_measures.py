import numpy as np

class YieldMeasures:
    def __init__(self, face_value, market_price, coupon_rate):
        self.market_price = market_price
        self.face_value = face_value
        self.coupon_rate = coupon_rate

    def current_yield(self):
        annual_cash_inflow = self.coupon_rate * self.face_value
        cy = annual_cash_inflow / self.market_price
        return cy

    def yield_to_maturity_zero(self, period):
        """
        N.B. Only valid for zero coupon bonds
        :param period: time to mature

        :return:
        """




        ym = ((self.face_value / self.market_price)**(1/period)) - 1
        return ym




bond = YieldMeasures(face_value=120, market_price=100, coupon_rate=0.05)
print(bond.current_yield())

print('\n')
print(bond.yield_to_maturity_zero(period = 2))
