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
st.title("Sessions")

if 'Login' not in st.session_state:
    st.session_state['Login'] = False

if 'Email' not in st.session_state:
    st.session_state['Email'] = False

if st.session_state["Login"]:
    
    st.write("This page shows upcoming sessions for this term!")
    queries = requests.get("http://127.0.0.1:5000/session").json()
    tournament_data = pd.DataFrame(queries["events"], columns=["Id", "Date", "Start", "End", "Location", "Participant Count", "Level" ])
    
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
        reformatted = str(datetime.strptime(row["Date"], "%Y-%m-%d"))
        event = dict()

        event["allDay"] = "true" # Cleaner formatting in calendar
        event["title"] = "Session " + row["Id"][2:] # Tournament Name, used as title in calendar
        event["start"] = reformatted.split()[0] + "T" +row["Start"] # Start date (used in calendar)
        event["key_start"] = reformatted.split()[0] + "T" +row["Start"] # Start date + time (used for tournament info)
        event["key_end"] = reformatted.split()[0] + "T" +row["End"] # Start date + time (used for tournament info)
        event["key"] = row["Participant Count"] # # of participants
        event["key2"] = row["Location"] # location of tournament
        event["key3"] = row["Id"] #EventId
        event["key4"] = row["Level"] #EventId
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

        # Add Session info
        st.title(tournament_info["title"])
        st.subheader("Time: %s to %s" % (tournament_info["extendedProps"]["key_start"].split("T")[1].split("-")[0], tournament_info["extendedProps"]["key_end"].split("T")[1].split("-")[0]))
        st.subheader("Location: %s" % (tournament_info["extendedProps"]["key2"]))
        st.subheader("Number of Participants: %s" % (tournament_info["extendedProps"]["key"]))
        st.subheader("Recommended Levels: %s" % (tournament_info["extendedProps"]["key4"]))

        registered_state = requests.get("http://127.0.0.1:5000/session_register?email=%s&session=%s&action=0" % (st.session_state["Email"], tournament_info["extendedProps"]["key3"])).json()["output"]

        if registered_state:
            if st.button("Unregister"):
                st.write("done")
                registered_state = requests.get("http://127.0.0.1:5000/session_register?email=%s&session=%s&action=2" % (st.session_state["Email"], tournament_info["extendedProps"]["key3"])).json()["output"]
        else:
            if st.button("Register", type = "primary"):
                st.write("done")
                registered_state = requests.get("http://127.0.0.1:5000/session_register?email=%s&session=%s&action=1" % (st.session_state["Email"], tournament_info["extendedProps"]["key3"])).json()["output"]


else:
    st.warning("Please Login to see this page")


set_session_tabs()

