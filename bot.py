import praw
import time
import smtplib, getpass

saved = {}

def check_for_updates():
    current = {}
    for submission in reddit.subreddit('buildapcsales').search(query='GPU', sort='new', limit=10):
        current[submission.id] = {submission.title: submission.shortlink}

    global saved
    if len(saved) == 0:
        saved = current.copy()
    else:
        current_ids = set(current)
        saved_ids = set(saved)
        difference = current_ids - saved_ids
        if len(difference) != 0:
            for id in difference:
                print(current[id])  # this is what going to be sent by mail
                saved[id] = current[id]
            ids_to_remove = saved_ids - current_ids
            for id in ids_to_remove:
                del saved[id]
    print(saved)

def set_smtp_connection(user, password, message):
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    try:
        smtpObj.login(user, password)
        smtpObj.sendmail(user, user, 'Subject: GPU sale update.\n\nSent from GPU-BOT')
    except smtplib.SMTPAuthenticationError:
        print('Wrong username or password')
    smtpObj.quit()


if __name__ == '__main__':
    reddit = praw.Reddit(client_id='nRhqSW1S9WfOdA', client_secret='CeQhsCuWYFinErouREl54koA89c', user_agent='bot')

    user = input('Email: ')
    password = input('Password: ')
    # password = getpass.getpass('Password: ')

    set_smtp_connection(user, password, 'HelloWorld!')

    # check_for_updates()
    # print(saved)
    # while 1:
    #     time.sleep(900)
    #     check_for_updates()

