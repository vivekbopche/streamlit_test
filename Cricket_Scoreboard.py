import streamlit as st

# Function to add a run to the score
def add_run(score, team, runs):
    score[team] += runs
    return score

# Function to add a wicket to the score
def add_wicket(wickets, team):
    wickets[team] += 1
    return wickets

# Main function to run the Streamlit app
def main():
    st.title("Cricket Scoreboard")

    # Initialize scores and wickets
    if "score" not in st.session_state:
        st.session_state.score = {"Team A": 0, "Team B": 0}
    
    if "wickets" not in st.session_state:
        st.session_state.wickets = {"Team A": 0, "Team B": 0}

    # Display current scores
    st.write(f"Team A: {st.session_state.score['Team A']} / {st.session_state.wickets['Team A']} wickets")
    st.write(f"Team B: {st.session_state.score['Team B']} / {st.session_state.wickets['Team B']} wickets")

    # Input for runs
    team = st.selectbox("Select Team", ("Team A", "Team B"))
    runs = st.number_input("Enter runs", min_value=0, max_value=6, step=1)
    if st.button("Add Runs"):
        st.session_state.score = add_run(st.session_state.score, team, runs)
        st.experimental_rerun()

    # Button for adding wicket
    if st.button("Add Wicket"):
        st.session_state.wickets = add_wicket(st.session_state.wickets, team)
        st.experimental_rerun()

    # Button for resetting scores
    if st.button("Reset Scores"):
        st.session_state.score = {"Team A": 0, "Team B": 0}
        st.session_state.wickets = {"Team A": 0, "Team B": 0}
        st.experimental_rerun()

if __name__ == "__main__":
    main()
