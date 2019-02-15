states={
    'Oreon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY'
}

for key,value in states.items():
    print key,value

exist=states.has_key('L')
print exist