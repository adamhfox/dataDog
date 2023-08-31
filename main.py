import streamlit as st

# UI Elements
st.title("Downtime Cost Calculator")
downtime_duration = st.slider("Downtime Duration (hours)", 0, 100, 1)
recovery_time = st.slider("Recovery Time (hours)", 0, 100, 1)
cost_per_hour = st.number_input("Cost per Hour ($)", 0, 100000, 1000)

# Calculations
total_downtime_cost = downtime_duration * cost_per_hour
total_recovery_cost = recovery_time * cost_per_hour
grand_total = total_downtime_cost + total_recovery_cost

formatted_downtime_cost = "{:,}".format(total_downtime_cost)
formatted_recovery_cost = "{:,}".format(total_recovery_cost)
formatted_grand_total = "{:,}".format(grand_total)


if grand_total > 10000:
    st.markdown(f"<h2 style='text-align: center; color: red;'>Total Downtime Cost: ${formatted_downtime_cost}</h2>", unsafe_allow_html=True)
elif grand_total > 5000:
    st.markdown(f"<h2 style='text-align: center; color: orange;'>Total Downtime Cost: ${formatted_downtime_cost}</h2>", unsafe_allow_html=True)
else:
    st.markdown(f"<h2 style='text-align: center; color: green;'>Total Downtime Cost: ${formatted_downtime_cost}</h2>", unsafe_allow_html=True)

st.markdown(f"<h2 style='text-align: center; color: blue;'>Total Recovery Cost: ${formatted_recovery_cost}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: purple;'>Grand Total Cost: ${formatted_grand_total}</h2>", unsafe_allow_html=True)


# Efficiency Gain Calculator UI
st.title("Efficiency Gain Calculator")
efficiency_gain = st.slider("Efficiency Gain (%)", 0, 100, 10)
operating_hours = st.slider("Operating Hours Per Week", 0, 168, 40)
weekly_revenue = st.number_input("Weekly Revenue ($)", 0, 10000000, 100000)

# Efficiency Gain Calculations
potential_gain = (efficiency_gain / 100) * weekly_revenue
annual_potential_gain = potential_gain * 52

# Display Efficiency Gain Results
st.markdown(f"<h2 style='text-align: center; color: blue;'>Potential Weekly Gain: ${'{:,}'.format(potential_gain)}</h2>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: green;'>Potential Annual Gain: ${'{:,}'.format(annual_potential_gain)}</h2>", unsafe_allow_html=True)