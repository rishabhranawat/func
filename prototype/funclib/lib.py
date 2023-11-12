import funclib.example as example
import funclib.news as news

import funclib.gmail_calendar as gmail_calendar
import funclib.gmail as gmail

def funcs():
    funcs = []
    funcs.extend(example.funcs())
    funcs.extend(news.funcs())
    funcs.extend(gmail_calendar.funcs())
    funcs.extend(gmail.funcs()) 

    return funcs   