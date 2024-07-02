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

if st.session_state["Login"]:
    
    st.write("This page shows upcoming tournaments for this term!")
    queries = requests.get("http://127.0.0.1:5000/session").json()
    team_data = pd.DataFrame(queries["teams"], columns=["TeamName", "TournamentName", "Date", "Start", "End", "Location"])
    tournament_data = pd.DataFrame(queries["events"], columns=["TournamentName", "Date", "Start", "End", "Location"])
    
    st.write(team_data)
    st.write(tournament_data)
    
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
    print("--")
    for ind, row in tournament_data.iterrows():
        event = dict()
        event["title"] = row["TournamentName"]
        reformatted = str(datetime.strptime(row["Date"], "%m/%d/%Y"))
        event["start"] = reformatted.split()[0] + " " +row["Start"]
        event["end"] = reformatted.split()[0] + " " +row["End"]
        calendar_events.append(event)
        print(reformatted)

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

    calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
    if calendar["callback"] == "eventClick":
        tournament_info = calendar["eventClick"]["event"]
        st.write(tournament_info)
        st.title(tournament_info["title"])
        st.write("**Time:** %s to %s" % (tournament_info["start"].split("T")[1].split("-")[0], tournament_info["end"].split("T")[1].split("-")[0]))
        st.write("**Location:** test")
else:
    st.warning("Please Login to see this page")


set_session_tabs()

