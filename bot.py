import praw
import time, os
import smtplib, getpass
from dotenv import load_dotenv


def check_for_updates(user, password, destination):
    current = {}
    for submission in reddit.subreddit('buildapcsales').search(query='GPU', sort='new', limit=10):
        current[submission.id] = '{}: {}'.format(submission.title, submission.shortlink)

    global saved
    if len(saved) == 0:
        saved = current.copy()
    else:
        current_ids = set(current)
        saved_ids = set(saved)
        difference = current_ids - saved_ids
        if len(difference) != 0:
            for id in difference:
                print('A new sale was posted! Sending email...')  # this is what going to be sent by mail
                set_smtp_connection(user, password, destination, current[id])
                print('Email was sent!')
                saved[id] = current[id]
            ids_to_remove = saved_ids - current_ids
            for id in ids_to_remove:
                del saved[id]


def set_smtp_connection(user, password, destination, message):
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    try:
        smtpObj.login(user, password)
        if message != 'check101':   # check connection - no need to send email yet
            smtpObj.sendmail(user, destination, 'Subject: GPU sale update.\n\n{}\n\nSent from GPU-BOT'.format(message))
    except smtplib.SMTPAuthenticationError:
        print('Wrong username or password')
    smtpObj.quit()


if __name__ == '__main__':

    path = os.path.join(os.getcwd(),'.env')
    load_dotenv(path)

    reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'], client_secret=os.environ['CLIENT_SECRET'], user_agent='bot')

    user = os.environ['USER_EMAIL']
    password = os.environ['USER_PASS']
    destination = os.environ['DESTINATION']

    set_smtp_connection(user,password,destination,'check101')   # check email credentials

    saved = {}

    check_for_updates(user, password, destination)
    print('Bot has started! No errors')

    while 1:
        time.sleep(900)
        check_for_updates(user, password, destination)
