import pandas as pd


class MemberLoan:

    def __init__(
        self,
        member_id,
        name,
        address,
        loan_amount,
        interest_rate,
        start_date
    ):

        self.member_id = member_id
        self.name = name
        self.address = address

        self.loan_amount = float(loan_amount)
        self.balance = float(loan_amount)

        # monthly interest
        self.rate = float(interest_rate) / 100

        self.start_date = start_date

        self.demand = []
        self.collection = []


    def add_payment(
        self,
        date,
        receipt_no,
        amount
    ):

        amount = float(amount)


        if self.balance <= 0:
            return



        # Opening balance
        opening_principal = self.balance



        # Interest calculation
        interest = (
            opening_principal *
            self.rate
        )



        # RULE A
        # Interest first

        if amount >= interest:

            interest_paid = interest

            principal_paid = (
                amount -
                interest
            )

        else:

            interest_paid = amount

            principal_paid = 0



        if principal_paid > self.balance:

            principal_paid = self.balance



        total_received = (
            principal_paid +
            interest_paid
        )



        # Demand Table

        self.demand.append({

            "Month": date,

            "Principal": round(
                opening_principal,2
            ),

            "Interest": round(
                interest,2
            ),

            "Total": round(
                opening_principal + interest,
                2
            )

        })



        # Collection Table

        self.collection.append({

            "Date": date,

            "Receipt No": receipt_no,

            "Principal": round(
                principal_paid,2
            ),

            "Interest": round(
                interest_paid,2
            ),

            "Total": round(
                total_received,2
            )

        })



        # Update balance LAST

        self.balance -= principal_paid



    def demand_df(self):

        return pd.DataFrame(
            self.demand
        )


    def collection_df(self):

        return pd.DataFrame(
            self.collection
        )



class SHG:


    def __init__(
        self,
        name,
        address
    ):

        self.name = name
        self.address = address

        self.members = {}



    def add_member(
        self,
        member
    ):

        self.members[
            member.member_id
        ] = member



    def get_member(
        self,
        member_id
    ):

        return self.members[member_id]