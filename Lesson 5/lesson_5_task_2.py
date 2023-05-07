#Напишите программу, которая примет в кач-ве аргумента integer (секунды)
# и вернет итоговое время в формате HH:MM:SS. Например: (seconds=3666) -> 01:01:06

seconds = int(input('Enter seconds: '))
hours = int(seconds / 3600)
minutes = int((seconds - (hours * 3600)) / 60)
seconds_new = int(seconds - (hours * 3600) - (minutes * 60))
if hours <= 9:
    hours = '0' + str(hours)
if minutes <= 9:
    minutes = '0' + str(minutes)
if seconds_new <= 9:
    seconds_new = '0' + str(seconds_new)
print(f'{hours}:{minutes}:{seconds_new}')