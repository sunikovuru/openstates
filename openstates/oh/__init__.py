import datetime

metadata = dict(
    name='Ohio',
    abbreviation='oh',
    legislature_name='Ohio Legislature',
    upper_chamber_name='Senate',
    lower_chamber_name='House of Representatives',
    upper_chamber_title='Senator',
    lower_chamber_title='Representative',
    upper_chamber_term=4,
    lower_chamber_term=2,
    terms=[
        {'name': '2009-2010', 'sessions': ['128'],
         'start_year': 2009, 'end_year': 2010},
        {'name': '2011-2012', 'sessions': ['129'],
         'start_year': 2011, 'end_year': 2012},
    ],
    session_details={
        '129': {'start_date': datetime.date(2011, 1, 3)},
        }
)