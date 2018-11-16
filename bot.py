import praw
import sched, time

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



s = sched.scheduler(time.time, time.sleep)
reddit = praw.Reddit(client_id='nRhqSW1S9WfOdA', client_secret='CeQhsCuWYFinErouREl54koA89c', user_agent='bot')

check_for_updates()
print(saved)
while 1:
    time.sleep(900)
    check_for_updates()

