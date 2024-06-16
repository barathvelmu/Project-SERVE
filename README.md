# Project-SERVE (CS 338, 2024)
Repository for the final project of Group 13 for CS338 (Spring 2024)

## Tech Stack
**Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Flask
- **Database:** SQlite (if it limits us after construction of the ER diagram, we can consider MySQL)
- **Visualization**: Pandas, Matplotlib

**Reasoning**
- **Streamlit:** easy to get the frontend working. Has prebuilt components and widgets for common tasks like adding buttons, sliders, text inputs. Jaden has working experience with it, so we will have some familiarity
- **Flask:** Jaden has working experience with Flask. I also have little Python web-dev experience so I can try to learn some Flask to code.
- **SQlite:** It is easy, very little configuration, recommended by the Project Document (CS 338), and is sheareable! 

## Running the Project
1. Ensure that you have all of the libraries installed as described in requirements.txt
2. Open Command Prompt / Terminal. Navigate to the "App" folder in the repository.
3. Launch the Flask API by running the command `python -m flask --app api run`.
4. Once the Flask API is running, open a new instance of Command Prompt / Terminal (keep the previous instance open). Navigate to the "App" folder and launch the Streamlit frontend by running the command `python -m streamlit run Home.py`.

**Please ensure that the file structure in the App folder is unchanged. Both the Flask API and the Streamlit frontend rely on the folder structure in order to run.**

## Note on Naming Commits
It would awesome if we could all write commit messages before pushing code changes/PRs, as it would help us know what the change is for!

**Example:** "_Wrote logic for button on home page_" or "_Added small HTML header for subtitle_"