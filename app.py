import streamlit as st

def getTax(amount) :
    tax = 0
    amount /= 10000;

    if(amount>25):
        amount -= 25
        if(amount<=25):
            tax = amount*0.05
        else :
            tax += (25*0.05)
            amount -= 25
            if (amount<=25):
                tax += (amount*0.1)
            else :
                tax += (25*0.1)
                amount -= 25
                if (amount<=25):
                    tax += (amount*0.15)
                else :
                    tax += (25*0.15)
                    amount -= 25
                    if (amount<=25):
                        tax += (amount*0.2)
                    else :
                        tax += (25*0.2)
                        amount -= 25
                        if (amount<=25):
                            tax += (amount*0.25)
                        else :
                            tax += (25*0.25)
                            amount -= 25
                            if amount>0 :
                                tax += (amount*0.3)

    tax *= 10000
    
    return tax


st.title("TAX CALCULATOR")

st.subheader("Enter Taxable Amount")

amt = st.number_input("", step=1000)
  
st.subheader("{:,}".format(int(getTax(amt))))