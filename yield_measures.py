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

    #def pure_discount_bounds(self):
        # pure disct. bonds info here


    #def Macaulay duration
        # Macaulay duration is the name given to the weighted average time until cash flows are received, and is measured in years.
        # Macaulay duration is a time measure with units in years, and really makes sense only for an instrument with fixed cash flows.
        # For a standard bond the Macaulay duration will be between 0 and the maturity of the bond. It is equal to the maturity if
        #  and only if the bond is a zero-coupon bond. (Source: Wiki)

        # The weight is introduced, because the yield of earlier coupon payments are less prone to interest rate fluctuations,
        # whereas coupon payments later in time are more sensitive to interest rate fluctuations.

        # Macaulay duration implementation here




