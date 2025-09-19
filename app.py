import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("Global_Fleet.csv")

# Title
st.title("✈️ Global Fleet Dashboard")

# Show Data
with st.expander("View Dataset"):
    st.dataframe(df)

# --- Filter by Region ---
regions = df["Region"].unique()
selected_region = st.selectbox("🌍 Select a Region", regions)

reg = df[df["Region"] == selected_region]

# --- Filter by Parent Airline ---
airlines = reg["ParentAirline"].unique()
selected_airline = st.selectbox("🛫 Select a Parent Airline", airlines)

pair = reg[reg["ParentAirline"] == selected_airline]

# --- Bar Plot: AircraftType vs Current ---
st.subheader(f"📊 Aircraft Fleet for {selected_airline} in {selected_region}")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sb.barplot(x=pair["AircraftType"], y=pair["Current"], ax=ax1, palette="viridis")
plt.xticks(rotation=90)
st.pyplot(fig1)

# --- Pie Chart: Region Distribution ---
st.subheader("🌍 Fleet Distribution by Region")
region_counts = df["Region"].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%', startangle=90)
ax2.axis("equal")
st.pyplot(fig2)
# --- Line Plot: Average Age by Region ---
st.subheader("📈 Average Age of Fleet by Region")
fig3, ax3 = plt.subplots(figsize=(10, 5))
sb.lineplot(x="Region", y="AverageAge", data=df, marker="o", ax=ax3, color="crimson")
plt.xticks(rotation=90)
st.pyplot(fig3)
