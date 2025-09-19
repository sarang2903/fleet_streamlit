import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Global Fleet Dashboard", page_icon="✈️", layout="wide")

# Load Data
df = pd.read_csv("Global_Fleet.csv")

# Title
st.title("✈️ Global Fleet Dashboard")
st.markdown("### 🌍 Explore the global airline fleet dataset with interactive charts")

# Sidebar filters
st.sidebar.header("🔎 Filters")
regions = df["Region"].unique()
selected_region = st.sidebar.selectbox("🌍 Select a Region", regions)

reg = df[df["Region"] == selected_region]

airlines = reg["ParentAirline"].unique()
selected_airline = st.sidebar.selectbox("🛫 Select a Parent Airline", airlines)

pair = reg[reg["ParentAirline"] == selected_airline]

# Dataset viewer
with st.expander("📑 View Raw Dataset"):
    st.dataframe(df)

# --- Bar Plot: AircraftType vs Current ---
st.subheader(f"📊 Aircraft Fleet for **{selected_airline}** in **{selected_region}**")
chart_type = st.radio("Choose Chart Type:", ["Bar", "Horizontal Bar", "Scatter"], horizontal=True)

fig1, ax1 = plt.subplots(figsize=(10, 5))
colors = plt.cm.viridis(range(len(pair)))

if chart_type == "Bar":
    ax1.bar(pair["AircraftType"], pair["Current"], color=colors)
    ax1.set_ylabel("Current Fleet")
elif chart_type == "Horizontal Bar":
    ax1.barh(pair["AircraftType"], pair["Current"], color=colors)
    ax1.set_xlabel("Current Fleet")
else:  # Scatter
    ax1.scatter(pair["AircraftType"], pair["Current"], color="crimson", s=120, edgecolor="black")
    ax1.set_ylabel("Current Fleet")

ax1.set_title("Aircraft Fleet Composition", fontsize=14, color="navy")
plt.xticks(rotation=90)
st.pyplot(fig1)

# --- Pie Chart: Region Distribution ---
st.subheader("🌍 Fleet Distribution by Region")
fig2, ax2 = plt.subplots(figsize=(6, 6))
colors = plt.cm.Paired(range(len(df["Region"].unique())))
region_counts = df["Region"].value_counts()
wedges, texts, autotexts = ax2.pie(region_counts.values,
                                   labels=region_counts.index,
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   colors=colors,
                                   wedgeprops={'edgecolor': 'white'})
plt.setp(autotexts, size=10, weight="bold", color="white")
ax2.set_title("Fleet Share by Region", fontsize=14, color="darkgreen")
ax2.axis("equal")
st.pyplot(fig2)

# --- Line Plot: Average Age by Region ---
st.subheader("📈 Average Age of Fleet by Region")
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.plot(df["Region"], df["AverageAge"], marker="o", color="crimson", linewidth=2, markersize=8)
ax3.set_xlabel("Region", fontsize=12)
ax3.set_ylabel("Average Age", fontsize=12)
ax3.set_title("Average Fleet Age", fontsize=14, color="darkred")
plt.xticks(rotation=45)
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("💡 *Interactive dashboard built with Streamlit & Matplotlib*")
