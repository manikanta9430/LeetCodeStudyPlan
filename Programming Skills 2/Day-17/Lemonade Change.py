class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_count = 0  # Count bills of 5
        ten_count = 0  # Count bills of 10
        for bill in bills:
            # No change to be given here
            # Since lemonade costs 5
            if bill == 5:
                five_count += 1
                continue
            # Give one 5 bill here as change
            # Add the 10 bill to our change box
            if bill == 10:
                # If we have no 5 bills, return False
                if five_count < 1:
                    return False
                ten_count += 1
                five_count -= 1
                continue
            # Give either three 5 bills here as change
            # Or give one 10 bill and one 5 bill as change
            # No real point keeping track of 20 bills
            # Since the problem does not accept them as change
            if bill == 20:
                # If we have have one 5 and one 10, give it as change
                if five_count >= 1 and ten_count >= 1:
                    ten_count -= 1
                    five_count -= 1
                    continue
                # If we have three 5s, give them as change
                if five_count >= 3:
                    five_count -= 3
                    continue
                # Otherwise, we do not have change for the customer
                return False
		# If everything goes as planned, we're good to go
        return True

