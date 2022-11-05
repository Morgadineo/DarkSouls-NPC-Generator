from random import choice
from quotes import *


# Get a random dark souls quote


def get_random_deletedquote():
    deleted_quote = choice(deleted_msg_quote)
    return deleted_quote


def get_random_name():
	name = choice(ds_names)
	title = choice(ds_titles)
	detail = choice(ds_details)
	person = f'{name} {title} {detail}'
	return person

	
def get_random_traces():
    traces = f'{choice(ds_traces)}, {choice(ds_traces)}, {choice(ds_traces)}'
    set(traces)
    while len(traces) < 3:
        if len(traces) < 3:
            traces.append(choice(ds_traces))
    return traces


def get_random_covenant():
    name = choice(ds_covenants_names)
    detail = choice(ds_covenants_details)
    covenant = f'{name} {detail}'
    return covenant


def get_random_npc():
    name = get_random_name()
    theme = choice(ds_themes)
    traces = get_random_traces()
    covenant = get_random_covenant()
    person = f'Name: {name}\nfeatures: {traces}\nTheme: {theme}\nGuild: {covenant}'
    return person

