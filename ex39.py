# Exercise 39: Dictionaries, Oh Lovely Dictionaries

# create a mapping of state to abbreviation
states = {
	'Alabama': 'AL',
	'Alaska': 'AK',
	'Arizona': 'AZ',
	'Arkansas': 'AR',
	'California': 'CA',
	'Colorado': 'CO',
	'Connecticut': 'CT',
	'Delaware': 'DE',
	'Florida': 'FL',
	'Georgia': 'GA',
	'Hawaii': 'HI',
	'Idaho': 'ID',
	'Illinois': 'IL',
	'Indiana': 'IN',
	'Iowa': 'IA',
	'Kansas': 'KS',
	'Kentucky': 'KY',
	'Louisiana': 'LA',
	'Maine': 'ME',
	'Maryland': 'MD',
	'Massachusetts': 'MA',
	'Michigan': 'MI',
	'Minnesota': 'MN',
	'Mississippi': 'MS',
	'Missouri': 'MO',
	'Montana': 'MT',
	'Nebraska': 'NE',
	'Nevada': 'NV',
	'New Hampshire': 'NH',
	'New Jersey': 'NJ',
	'New Mexico': 'NM',
	'New York': 'NY',
	'North Carolina': 'NC',
	'North Dakota': 'ND',
	'Ohio': 'OH',
	'Oklahoma': 'OK',
	'Oregon': 'OR',
	'Pennsylvania': 'PA',
	'Rhode Island': 'RI',
	'South Carolina': 'SC',
	'South Dakota': 'SD',
	'Tennessee': 'TN',
	'Texas': 'TX',
	'Utah': 'UT',
	'Vermont': 'VT',
	'Virginia': 'VA',
	'Washington': 'WA',
	'West Virginia': 'WV',
	'Wisconsin': 'WI',
	'Wyoming': 'WY'
}

# create a mapping of state abbreviation to state capitol
capitols = {
	'AL': 'Montgomery',
	'AK': 'Juneau',
	'AZ': 'Phoenix',
	'AR': 'Little Rock',
	'CA': 'Sacramento',
	'CO': 'Denver',
	'CT': 'Hartford',
	'DE': 'Dover',
	'FL': 'Tallahassee',
	'GA': 'Atlanta',
	'HI': 'Honolulu',
	'ID': 'Boise',
	'IL': 'Springfield',
	'IN': 'Indianapolis',
	'IA': 'Des Moines',
	'KS': 'Topeka',
	'KY': 'Frankfort',
	'LA': 'Baton Rouge',
	'ME': 'Augusta',
	'MD': 'Annapolis',
	'MA': 'Boston',
	'MI': 'Lansing',
	'MN': 'St. Paul',
	'MS': 'Jackson',
	'MO': 'Jefferson City',
	'MT': 'Helena',
	'NE': 'Lincoln',
	'NV': 'Carson City',
	'NH': 'Concord',
	'NJ': 'Trenton',
	'NM': 'Santa Fe',
	'NY': 'Albany',
	'NC': 'Raleigh',
	'ND': 'Bismarck',
	'OH': 'Columbus',
	'OK': 'Oklahoma City',
	'OR': 'Salem',
	'PA': 'Harrisburg',
	'RI': 'Providence',
	'SC': 'Columbia',
	'SD': 'Pierre',
	'TN': 'Nashville',
	'TX': 'Austin',
	'UT': 'Salt Lake City',
	'VT': 'Montpelier',
	'VA': 'Richmond',
	'WA': 'Olympia',
	'WV': 'Charleston',
	'WI': 'Madison',
	'WY': 'Cheyenne'
}

# print out some capitols
print '-' * 10
print 'NY has: ', capitols['NY']
print 'OR has: ', capitols['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it using the state then capitols dict
print '-' * 10
print 'Michigan has: ', capitols[states['Michigan']]
print 'Florida has: ', capitols[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s." % (state, abbrev)

# print every state capitol
print '-' * 10
for abbrev, capitol in capitols.items():
	print "%s has the capitol %s." % (abbrev, capitol)

# now do both simultaneously
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s and has its capitol in %s." % (
		state, abbrev, capitols[abbrev])

# safely get an abbreviation for a territory not in the list
print '-' * 10
territory = states.get('Guam', None)

if not territory:
	print "Sorry, no Guam."

# get a city with a default value
city = capitols.get('GU', 'Does Not Exist')
print "The city for 'GU' is: %s" % city
