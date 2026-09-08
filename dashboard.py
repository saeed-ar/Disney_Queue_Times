import streamlit as st 
import pandas as pd

st.title("Disney Wait Times Dashboard")
st.write("Hello, Streamlit!")
st.write("testing")

df = pd.read_csv("all_park_data.csv")



avg_wait = df.groupby("park_name")["wait_time"].mean()

avg_wait_time = avg_wait[avg_wait > 0]
    
st.subheader("Average Wait Time by Park")
st.bar_chart(avg_wait_time, x_label="Park", y_label="Average Wait Time (min)")

longest_avg_wait_park = avg_wait_time.idxmax()
longest_avg_wait_time = max(avg_wait_time)

st.write(f"{longest_avg_wait_park} has the longest average wait time: {longest_avg_wait_time} minutes")

shortest_avg_wait_park = avg_wait_time.idxmin()
shortest_avg_wait_time = min(avg_wait_time) 


st.write(f"{shortest_avg_wait_park} has the shortest average wait time: {shortest_avg_wait_time} minutes")




st.subheader("Average Wait Time by Ride Per Park")

for park in df["park_name"].unique():
    park_df = df[df["park_name"] == park]
    ride_avg_wait = park_df.groupby("ride_name")["wait_time"].mean()
    ride_avg_wait = ride_avg_wait[ride_avg_wait > 0]
    if ride_avg_wait.empty:
        continue
    st.subheader(f"Average Wait Time by Ride Per Park: {park}")
    st.bar_chart(ride_avg_wait)

