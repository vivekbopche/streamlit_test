import streamlit as st

# Function to add a run to the score
def add_run(score, team, runs):
    score[team] += runs
    return score

# Function to add a wicket to the score
def add_wicket(wickets, team):
    if wickets[team] < 10:
        wickets[team] += 1
    else:
        st.warning(f"{team} has already lost 10 wickets!")
    return wickets

# Main function to run the Streamlit app
def main():
    st.title("Cricket Scoreboard")

    # Initialize scores and wickets
    if "score" not in st.session_state:
        st.session_state.score = {"Team A": 0, "Team B": 0}
    
    if "wickets" not in st.session_state:
        st.session_state.wickets = {"Team A": 0, "Team B": 0}

    if "overs" not in st.session_state:
        st.session_state.overs = st.slider("Select number of overs for the match", 1, 50, 20)

    if "current_over" not in st.session_state:
        st.session_state.current_over = {"Team A": 0, "Team B": 0}
    
    # Display current scores and overs
    st.write(f"Team A: {st.session_state.score['Team A']} / {st.session_state.wickets['Team A']} wickets")
    st.write(f"Overs: {st.session_state.current_over['Team A']} / {st.session_state.overs}")
    st.write(f"Team B: {st.session_state.score['Team B']} / {st.session_state.wickets['Team B']} wickets")
    st.write(f"Overs: {st.session_state.current_over['Team B']} / {st.session_state.overs}")

    # Input for runs
    team = st.selectbox("Select Team", ("Team A", "Team B"))
    runs = st.number_input("Enter runs", min_value=0, max_value=6, step=1)
    if st.button("Add Runs"):
        st.session_state.score = add_run(st.session_state.score, team, runs)
        st.experimental_rerun()

    # Input for adding a ball
    if st.button("Add Ball"):
        if st.session_state.current_over[team] < st.session_state.overs:
            st.session_state.current_over[team] += 0.1
            if st.session_state.current_over[team] % 1 >= 0.6:
                st.session_state.current_over[team] = (st.session_state.current_over[team] // 1) + 1
            st.experimental_rerun()
        else:
            st.warning(f"{team} has completed {st.session_state.overs} overs!")

    # Button for adding wicket
    if st.button("Add Wicket"):
        st.session_state.wickets = add_wicket(st.session_state.wickets, team)
        st.experimental_rerun()

    # Button for resetting scores
    if st.button("Reset Scores"):
        st.session_state.score = {"Team A": 0, "Team B": 0}
        st.session_state.wickets = {"Team A": 0, "Team B": 0}
        st.session_state.current_over = {"Team A": 0, "Team B": 0}
        st.experimental_rerun()

if __name__ == "__main__":
    main()
