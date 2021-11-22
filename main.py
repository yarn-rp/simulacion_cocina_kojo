

from problema import problem


clients_wait_time = problem(True)
total_time = sum(clients_wait_time)
less_than_expected = 0
for i in clients_wait_time:
    if (i >= 5*60):
        less_than_expected += i
print("3 trabajadores", total_time, (less_than_expected/total_time)*100)

clients_wait_time = problem(False)
total_time = sum(clients_wait_time)
less_than_expected = 0
for i in clients_wait_time:
    if (i >= 5*60):
        less_than_expected += i
print("2 trabajadores", total_time, (less_than_expected/total_time)*100)
