import praw
import time
import smtplib, getpass

saved = {}


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
                print(current[id])  # this is what going to be sent by mail
                set_smtp_connection(user, password, destination, current[id])
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
        smtpObj.sendmail(user, destination, 'Subject: GPU sale update.\n\n{}\n\nSent from GPU-BOT'.format(message))
    except smtplib.SMTPAuthenticationError:
        print('Wrong username or password')
    smtpObj.quit()


if __name__ == '__main__':
    reddit = praw.Reddit(client_id='nRhqSW1S9WfOdA', client_secret='CeQhsCuWYFinErouREl54koA89c', user_agent='bot')

    user = input('Email: ')
    password = getpass.getpass()
    destination = input('Destination: ')

    check_for_updates(user, password, destination)
    # print(saved)
    while 1:
        time.sleep(900)
        check_for_updates(user, password, destination)
