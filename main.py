import streamlit as st

st.title("Nike Run Club App")

# Sidebar options
lap_duration = st.sidebar.slider("Lap Duration (minutes)", 1, 60, 5)
selected_pace = st.sidebar.selectbox("Select Pace", ["10km", "5km", "Mile", "Best", "Warmup", "Recovery"])

# Pace dictionary
paces = {
    "10km": ("10 kilometer pace", 6.2),
    "5km": ("5 kilometer pace", 3.1),
    "Mile": ("Mile pace", 1.0),
    "Best": ("Your best pace", None),
    "Warmup": ("Warm-up pace", None),
    "Recovery": ("Recovery pace", None),
}

if selected_pace in paces:
    pace, pace_length = paces[selected_pace]
    if pace_length:
        lap_length = lap_duration / pace_length
        st.write(f"Selected Pace: {pace}")
        st.write(f"Lap Length: {lap_length:.2f} kilometers")

    st.write("Start running and use the app for announcements.")

else:
    st.write("Select a valid pace from the sidebar.")
