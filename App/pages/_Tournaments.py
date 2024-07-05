import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd
from Home import set_session_tabs
from st_pages import Page, show_pages, hide_pages
from streamlit_calendar import calendar
from datetime import datetime

#hide_pages(["Home"])
#st.set_page_config(page_title="Students", page_icon="🏐")
st.sidebar.image("logo.png")
st.sidebar.markdown("<h1 style='text-align: center;'>UW SERVE</h1>", unsafe_allow_html=True)
st.title("Tournaments")

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

if 'Exec' not in st.session_state:
    st.session_state['Exec'] = False

if st.session_state["Login"]:
    
    st.write("This page shows upcoming tournaments for this term!")
    queries = requests.get("http://127.0.0.1:5000/tournament").json()
    tournament_data = pd.DataFrame(queries["events"], columns=["TournamentName", "Date", "Start", "End", "Location", "Id"])
    
    calendar_options = {
        "editable": "false",
        "selectable": "true",
        "headerToolbar": {
            "left": "prev,next",
            "center": "title",
            "right": "today",
        },
        "displayEventTime": "false",

    }

    calendar_events = []

    for ind, row in tournament_data.iterrows():
        reformatted = str(datetime.strptime(row["Date"], "%m/%d/%Y"))
        event = dict()

        event["allDay"] = "true" # Cleaner formatting in calendar
        event["title"] = row["TournamentName"] # Tournament Name, used as title in calendar
        event["start"] = reformatted.split()[0] + "T" +row["Start"] # Start date (used in calendar)
        event["key_start"] = reformatted.split()[0] + "T" +row["Start"] # Start date + time (used for tournament info)
        event["key_end"] = reformatted.split()[0] + "T" +row["End"] # Start date + time (used for tournament info)
        event["key"] = row["Id"] # EventId associated with tournament (used for tournament_info endpoint)
        event["key2"] = row["Location"] # location of tournament
        calendar_events.append(event)

    custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """

    calendar = calendar(events=calendar_events, options=calendar_options)

    if calendar["callback"] == "eventClick":
        tournament_info = calendar["eventClick"]["event"]

        # Add tournament info
        st.title(tournament_info["title"])
        st.subheader("Time: %s to %s" % (tournament_info["extendedProps"]["key_start"].split("T")[1].split("-")[0], tournament_info["extendedProps"]["key_end"].split("T")[1].split("-")[0]))
        st.subheader("Location: %s" % (tournament_info["extendedProps"]["key2"]))

        # Add teams to view
        team_info = requests.get("http://127.0.0.1:5000/team_info?Id="+tournament_info["extendedProps"]["key"]).json()
        team_df = pd.DataFrame(team_info["teams"], columns=["Name", "Level", "Team"])
        for team in team_df["Team"].unique():
            with st.expander(":red[%s]" % team):
                team_members = team_df[team_df["Team"] == team][["Name", "Level"]]
                for ind, row in team_members.iterrows():
                    st.write("%s, Level %s" % (row["Name"], row["Level"]))
else:
    st.warning("Please Login to see this page")


set_session_tabs()

