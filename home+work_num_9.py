#START Question 1
temp: list[float] = []
num = 0

while num != -999:
    num: float = float(input("Enter a temperature: "))
    if -50 < num < 50:
        temp.append(num)

print(temp)

temp.extend([-20.0, 39.1, 18.5])
print(temp)

#1d answer = ההבדך בין extend ל+ הוא שהחיבור יוצר רשימה חדשה לגמרי אבל ה-extent משנה את הרשימה כולה

print(f"Highest temperature: {max(temp)}")
print(f"Lowest temperature: {min(temp)}")

if 18.5 in temp:
    print("True")
else:
    print("False")

print(f"-20.0 appears {temp.count(-20.0)} times")

average= sum(temp) / len(temp) if temp else 0
print(f"Average temperature: {average}")

for i in temp:
    print(i)

if 39.1 in temp:
    print(f"Index of 39.1: {temp.index(39.1)}")

del temp[0]
print("Temperatures after removing the first element:", temp)

for i in range(len(temp) - 1, -1, -1):
    if i % 2 == 0:
        del temp[i]
print(temp)

if 18.5 in temp:
    temp.remove(18.5)
    print("Temperatures after removing 18.5:", temp)
else:
    print("18.5 not found in the list")

#Question 1m = אם לא נבדוק קודם את המספר בתוך המערך וישר נעשה remove כי במספר עצמו לא שם זה יכול לעשות Error

last_temp = temp.pop()
print(f"Last temperature: {last_temp}")

temp_copy = temp.copy()
temp_copy.sort()
print("Sorted copy of the temperatures:", temp_copy)

temp_copy_reverse = temp.copy()
temp_copy_reverse.sort(reverse=True)
print("Reverse sorted copy of the temperatures:", temp_copy_reverse)
#END

#START 2
numbers = []
while True:
    num = float(input("Enter a number between 0 and 10: "))
    if num == -999:
        break
    elif 0 <= num <= 10:
        numbers.append(num)

        stats = {}
        for i in range(11):
            count = numbers.count(i)
            if count > 0:
                stats[i] = count

        print("Statistics:", [f"[{key}] : {value}" for key, value in stats.items()])
#END

#START 3
import random

range_min = 0
range_max = 10
samples = 100

stats = [0] * (range_max + 1)

for _ in range(samples):
    number = random.randint(range_min, range_max)
    stats[number] += 1

for number in range(len(stats)):
    print(f"{number}: {stats[number]} times")
#END

