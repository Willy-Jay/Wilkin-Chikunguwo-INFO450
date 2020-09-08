def check_users(current_users, new_users):

    pass
#I renamed the lists from current_us to current_users and new_us to new_users
current_users = ['chris','haritha', 'sally', 'darnell', 'SUPERMAN']

new_users = ['george', 'ringo', 'superman', 'hannibal']
#Cool kid way of doing it.
new_list =[]
for current_user in current_users:
    new_list.append(current_user.lower())

current_users = [itm.lower() for itm in current_users]

for new_user in new_users:
    if  new_user in current_users:
        print(f'Sorry the username {new_user} is already taken.Please create a new username.')
    else:
        print(f'The username {new_user} is availble.')
if __name__ == "__main__":
# I added 'ers' to current_us and new_us.
# I also moved the current_users and new_users list to lines 5 and 7.
 check_users(current_users, new_users)
