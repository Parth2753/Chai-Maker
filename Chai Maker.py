import streamlit as st
st.title("Chai Maker App")
if st.button("Make Chai"):
    st.success("Your chai is being brewed")
chai= st.checkbox("Add Chai powder")
if chai:
    st.write("Chai powder is added to your chai")

tea_type = st.radio("Pick your chai base: ", ["Milk","Water","Badam Milk"])

st.write(f"Selected base:  {tea_type} is selected ")
flavour = st.selectbox("Choose: ", ["adrak","Kesar"])
st.write(f"Selected flavour: {flavour}")
sugar = st.slider("Sugar (spoon)",0,2,5)
st.write(f"Selected sugar spoon: {sugar} is selected")
cups= st.number_input("How many cups",min_value=0,max_value=10,step=1)
st.write(f"Selected cups: {cups} is selected")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name}! Your chai is on the way")

dob = st.date_input("Select your date of birth: ")
st.write(f"Your date of birth is: {dob}")