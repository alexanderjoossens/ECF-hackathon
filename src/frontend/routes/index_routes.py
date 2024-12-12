import os, sys
import time

# # #following 2 lines are to use vaderSentiment here
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../vaderSentiment/vaderSentiment')))
# from vaderSentiment.vaderSentiment import start

# Hardcoding the absolute path to the vaderSentiment folder
# sys.path.append('/Users/alexanderjoossens/Documents/Github/vaderSentiment/vaderSentiment')

# from vaderSentiment.vaderSentiment import start
print('start succesfully imported')


from flask import render_template, redirect, request, session, Blueprint, current_app, url_for

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from src.frontend.utils.usage_logger import UsageLogger


# -------------------------------------------------------------------------------------------------------------------------------------------

logger = UsageLogger()

index_blueprint = Blueprint('index-blueprint', __name__, template_folder='../templates/index')

@index_blueprint.route('/')
def main_page():
    session.clear()

    logger.health_log_message("None", "Landed on homepage")

    return render_template("homepage.html")

@index_blueprint.route('/', methods=['POST'])
def main_page_post():
    # Step 1.1: Retrieve the session-id from the form input
    session_id = request.form['session-id']
    
    # Step 1.2: Create a timestamp (optional for uniqueness or other purposes)
    session_timestamp = time.time()
    session_id_with_timestamp = session_id + "|" + str(session_timestamp)
    
    # Step 1.3: Store the session data in Flask's session object
    session["session-id"] = session_id_with_timestamp

    # Step 1.4: Log the health message
    logger.health_log_message(session_id, "Filled in session ID: [" + session_id + "] with Timestamp: [" + str(session_timestamp) + "]")

    # Step 1.5: Redirect to the next page (qr-page)
    return redirect(url_for('index-blueprint.qr_page'))

@index_blueprint.route('/qr-page')
def qr_page():
    # current_directory = os.getcwd()
    # print('-')
    # print('-')
    # print("Current Directory: ", current_directory)
    # # get parent directory of current directory:
    # three_directories_up = os.path.abspath(os.path.abspath(os.path.abspath(os.path.join(current_directory, os.pardir))))
    # print("Three directories up: ", three_directories_up)
    # path_to_vaderSentiment = os.path.join(three_directories_up, 'vaderSentiment', 'vaderSentiment.py')
    # path_to_vaderSentiment = "/Users/alexanderjoossens/Documents/Github/vaderSentiment/vaderSentiment/vaderSentiment.py"
    # print('path_to_vaderSentiment:', path_to_vaderSentiment)


    # # Step 2.1: Retrieve the session-id stored earlier
    session_id_with_timestamp = session.get('session-id', None)
    # articles_analysed = start()





    # Step 2.2: Pass the session data to the template (qr_page.html)
    return render_template('qr_page.html', session_id=session_id_with_timestamp)
    # return render_template('qr_page.html', session_id=articles_analysed)