# Project-SERVE 🚀

## Demo Videos
Note: all links do not open in a new tab natively
- Milestone 1 Demo: https://youtu.be/dOFKvirQiRU 
- Milestone 2 Demo: https://youtu.be/ydMeBrlFJ-0
  - Added features are shown in the 2nd half of the video (up till the end).
- **Final Report Demo:** [Here](https://youtu.be/KRG7l4a9HeQ?si=NFepZL0Zref-svRQ)

## Features Currently Supported
- Viewing Aggregate Statisics of the SERVE Club *by Faculty, Gender, and Level* ("Student Breakdown")
- Email-based Authentication: register and login
- Adding a club member (with form validation logic)
- Updating a club member (with form validation logic)
- Dynamic sidebar based on login/logout (purely code based)
- View and register for upcoming sessions
- View previous and upcoming tournaments, as well as the teams participating in them.

## Running the Project
1. Ensure that you have all of the libraries installed as described in requirements.txt using `pip install -r requirements.txt`
2. As our team is using SQLite for the database, there are no additional steps to set it up! It is already accounted for by continuing with the next steps.
3. Open Command Prompt / Terminal. Navigate to the "App" folder in the repository - `cd App`.
4. Launch the Flask API (backend) by running the command `python -m flask --app api run`.
5. Once the Flask API is running, open a new instance of Command Prompt / Terminal. Please keep the previous instance open as the backend and frontend have to run simultaneously.
6. Navigate to the "App" folder and launch the Streamlit (frontend) by running the command `python -m streamlit run Tabs.py`.

**Please ensure that the file structure in the App folder is unchanged. Both the Flask API and the Streamlit frontend rely on the folder structure in order to run.**

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Flask
- **Database:** SQLite 
- **Visualization**: Pandas, Matplotlib

## Note on Commits
Our team did our best to name our code commits. 
**Example:** "_Wrote logic for button on home page_" or "_Added small HTML header for subtitle_"
