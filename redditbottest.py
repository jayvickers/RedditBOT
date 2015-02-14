import praw
user_agent = 'user subreddit submission history bot v1.0 (by MYUSER)'
r = praw.Reddit(user_agent=user_agent)
r.login('bot_username', 'bot_password')
subreddit = r.get_subreddit('test')
subreddit_comments = subreddit.get_comments()
flat_comments = praw.helpers.flatten_tree(subreddit_comments)
keyWord = '!testerinomyboterino'
already_replied = set()
for comment in flat_comments
    if keyWord in comment.body and comment.id not in already_replied:
        submission = comment.submission
        username = submission.author
        msg = '[username of author] ' + username + '  did it work?'
        r.send_message('infinite__recursion', 'my bot test 1', msg)
        already_replied.append(submission.id)