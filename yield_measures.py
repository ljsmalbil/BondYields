import numpy as np

class YieldMeasures:
    def __init__(self, face_value, market_price, coupon_rate):
        self.market_price = market_price
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.coupon_value = face_value * coupon_rate

    def current_yield(self):
        annual_cash_inflow = self.coupon_rate * self.face_value
        cy = annual_cash_inflow / self.market_price
        return cy

    def yield_to_maturity(self, n, sensitivity = 0.0001):
        """
        N.B. This function estimates the YTM parameter.

        :param period: time to maturity

        :return: YTM
        """
        # bond_price = (coupon_value * ((1 - (1/((1 + YTM)**n)))/YTM)) + (face_value * (1/(1 + YTM)**n))

        # Create an interval
        bond_price = 0
        YTM_pos = 0.0001
        YTM_neg = -0.0001

        # N.B. Sensitivity is important here
        lower_bound = self.market_price - (self.market_price * sensitivity)
        upper_bound = self.market_price + (self.market_price * sensitivity)

        # print(lower_bound < bond_price < upper_bound)

        while (lower_bound < bond_price < upper_bound) == False:
            # Bond trades at discount
            if self.face_value > self.market_price:
                bond_price = (self.coupon_value * ((1 - (1 / ((1 + YTM_pos) ** n))) / YTM_pos)) + (
                            self.face_value * (1 / (1 + YTM_pos) ** n))
                YTM_pos += 0.0001

            # Bond trades at premium
            else:
                bond_price = (self.coupon_value * ((1 - (1 / ((1 + YTM_neg) ** n))) / YTM_neg)) + (
                            self.face_value * (1 / (1 + YTM_neg) ** n))
                YTM_neg -= 0.0001

        if YTM_pos == 0.0001:
            return YTM_neg
        else:
            return YTM_pos




