# STACKS (LIFO)

# adding item on top each other
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# removing item on every on top
browsing_session.pop()
browsing_session.pop()
if not browsing_session: # falsy 
    browsing_session[-1]
print(browsing_session)