import streamlit as st
import pandas as pd

from loan_manage import MemberLoan, SHG



st.set_page_config(
    page_title="SHG Loan Ledger",
    layout="wide"
)



st.title("🏦 SHG Loan Ledger System")



# -------------------------
# Session storage
# -------------------------

if "shg" not in st.session_state:

    st.session_state.shg = SHG(
        "My SHG",
        "Address"
    )



menu = st.sidebar.selectbox(

    "Menu",

    [
        "Create Member",
        "Add Collection",
        "View Ledger"
    ]

)



# =========================
# CREATE MEMBER
# =========================

if menu == "Create Member":


    st.header(
        "Member Loan Details"
    )


    member_id = st.text_input(
        "Member Number"
    )


    name = st.text_input(
        "Member Name"
    )


    address = st.text_input(
        "Address"
    )


    loan = st.number_input(
        "Loan Amount",
        min_value=0.0
    )


    interest = st.number_input(
        "Monthly Interest (%)",
        min_value=0.0
    )


    date = st.text_input(
        "Loan Start Date"
    )



    if st.button("Add Member"):


        member = MemberLoan(

            member_id,

            name,

            address,

            loan,

            interest,

            date

        )


        st.session_state.shg.add_member(
            member
        )


        st.success(
            "Member Added Successfully"
        )




# =========================
# ADD PAYMENT
# =========================


elif menu == "Add Collection":


    st.header(
        "Collection Entry"
    )


    members = list(
        st.session_state.shg.members.keys()
    )


    if len(members)==0:

        st.warning(
            "Add member first"
        )

    else:


        selected = st.selectbox(
            "Select Member",
            members
        )


        date = st.text_input(
            "Payment Date"
        )


        receipt = st.text_input(
            "Receipt Number"
        )


        amount = st.number_input(
            "Amount Received",
            min_value=0.0
        )



        if st.button(
            "Save Payment"
        ):


            member = (
                st.session_state
                .shg
                .get_member(selected)
            )


            member.add_payment(

                date,

                receipt,

                amount

            )


            st.success(
                "Payment Saved"
            )





# =========================
# VIEW LEDGER
# =========================


elif menu == "View Ledger":


    st.header(
        "Loan Ledger"
    )


    for member_id, member in st.session_state.shg.members.items():


        st.subheader(
            member.name
        )


        col1,col2 = st.columns(2)



        with col1:


            st.write(
                "Demand / Installment Due"
            )


            st.dataframe(
                member.demand_df()
            )



        with col2:


            st.write(
                "Collection / Recovery"
            )


            st.dataframe(
                member.collection_df()
            )


        st.divider()