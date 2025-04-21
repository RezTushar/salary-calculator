import streamlit as st

# Title
st.title("Salary Calculator (RON)")

# Input: Net Salary
net_salary = st.number_input("Net Salary (RON)", min_value=0.0, step=0.01)

# Input: Total Regular Work Hours (Allow decimal input like 10.5)
total_hours = st.number_input("Total Regular Work Hours", min_value=0.0, step=0.01)

# Calculate Hourly Rate
hourly_rate = net_salary / total_hours if total_hours != 0 else 0

# Display Hourly Rate (readonly)
st.text_input("Hourly Rate (Auto-calculated in RON)", value=f"{hourly_rate:.2f}", disabled=True)

# Input: Night Hours during the Week
night_hours_week = st.number_input("Night Hours during the Week", min_value=0.0, step=0.01)

# Input: Day Hours during the Weekend
day_hours_weekend = st.number_input("Day Hours during the Weekend", min_value=0.0, step=0.01)

# Input: Night Hours during the Weekend
night_hours_weekend = st.number_input("Night Hours during the Weekend", min_value=0.0, step=0.01)

# Input: Holiday Hours
holiday_hours = st.number_input("Holiday Hours", min_value=0.0, step=0.01)

# Input: Overtime Hours (allow decimal input for extra hours worked)
overtime_hours = st.number_input("Overtime Hours", min_value=0.0, step=0.01)

# Input: Performance Bonus
performance_bonus = st.number_input("Performance Bonus (RON)", min_value=0.0, step=0.01)

# Calculate Bonuses
night_week_bonus = hourly_rate * 0.25 * night_hours_week
day_weekend_bonus = hourly_rate * 0.15 * day_hours_weekend
night_weekend_bonus = hourly_rate * 0.40 * night_hours_weekend
holiday_bonus = hourly_rate * 1 * holiday_hours
overtime_bonus = hourly_rate * 1.75 * overtime_hours  # Overtime Bonus Calculation

# Calculate Total Salary
total_salary = (net_salary + night_week_bonus + day_weekend_bonus + night_weekend_bonus + 
                holiday_bonus + overtime_bonus + performance_bonus)

# Display Results
st.subheader("Salary Breakdown")
st.markdown(f"- Hourly Rate: `{hourly_rate:.2f} RON`")
st.markdown(f"- Night Week Bonus: `{night_week_bonus:.2f} RON`")
st.markdown(f"- Day Weekend Bonus: `{day_weekend_bonus:.2f} RON`")
st.markdown(f"- Night Weekend Bonus: `{night_weekend_bonus:.2f} RON`")
st.markdown(f"- Holiday Bonus: `{holiday_bonus:.2f} RON`")
st.markdown(f"- Overtime Bonus: `{overtime_bonus:.2f} RON`")  # Overtime Bonus Breakdown
st.markdown(f"- Performance Bonus: `{performance_bonus:.2f} RON`")

st.subheader("💰 Total Salary")
st.success(f"💰 Total Salary: {total_salary:.2f} RON")
