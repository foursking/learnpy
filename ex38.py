#create a mapping of state to abbreviation

states = {
    'Oregon'     : 'OR',
    'Florida'    : 'FL',
    'California' : 'CA',
    'New York'   : 'NY',
    'Michigan'   : 'MI',
}

#create a bask set of states and some cities in them

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville',
}

print (states)

exit(0)


#add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: " , cities['NY']
print "OR State has: " , cities['OR']

#print some states
print '-' * 10

for state , abbrev in states.items():
    print "%s has the city %s" % (state , abbrev)


