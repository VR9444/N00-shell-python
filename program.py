import os
from datetime import datetime
import random

def read_score(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return int(f.read().strip())
    else:
        print(f"File {filename} does not exist.")
        return 0

def create_file_with_random_number(filename, min_num, max_num):
    with open(filename, 'w') as f:
        f.write(str(random.randint(min_num, max_num)))

filenames = [
    'Ns-Intro.txt', 'Ni-SYCL.txt', 'N00-Shell.txt', 'N01-Linux-VM.txt', 'N02-Linux-Cluster.txt',
    'N03-MPI-PingPong.txt', 'N04-MPI-Cluster.txt', 'N05-Sync.txt', 'N06-Control.txt', 
    'N07-Hadoop-Single.txt', 'N08-Hadoop-Cluster.txt', 'N09-Map.txt', 'N10-Reduce.txt',
    'N11-Docker.txt'
]

probability_of_number = 0.5

for filename in filenames:
    if random.random() < probability_of_number:
        create_file_with_random_number(filename, 10, 12)
    else:
        with open(filename, 'w') as f:
            f.write('0')

create_file_with_random_number('K1.txt', 0, 100)
create_file_with_random_number('K2.txt', 0, 100)
create_file_with_random_number('BonusSodelovanje.txt', 0, 20)
create_file_with_random_number('Izpit.txt', 0,100)


Ns = read_score('Ns-Intro.txt')
Ni = read_score('Ni-SYCL.txt')
N00 = read_score('N00-Shell.txt')
N01 = read_score('N01-Linux-VM.txt')
N02 = read_score('N02-Linux-Cluster.txt')
N03 = read_score('N03-MPI-PingPong.txt')
N04 = read_score('N04-MPI-Cluster.txt')
N05 = read_score('N05-Sync.txt')
N06 = read_score('N06-Control.txt')
N07 = read_score('N07-Hadoop-Single.txt')
N08 = read_score('N08-Hadoop-Cluster.txt')
N09 = read_score('N09-Map.txt')
N10 = read_score('N10-Reduce.txt')
N11 = read_score('N11-Docker.txt')
Bonus = read_score('BonusSodelovanje.txt')
bonus_vaje = 0
Izpit = read_score('Izpit.txt')


def check_and_cap_score(score):
    if score > 10:
        bonus = score - 10
        return 10, bonus
    return score, 0

bonus_vaje = 0

filenames = [
    'Ns-Intro.txt', 'Ni-SYCL.txt', 'N00-Shell.txt', 'N01-Linux-VM.txt', 'N02-Linux-Cluster.txt',
    'N03-MPI-PingPong.txt', 'N04-MPI-Cluster.txt', 'N05-Sync.txt', 'N06-Control.txt', 
    'N07-Hadoop-Single.txt', 'N08-Hadoop-Cluster.txt', 'N09-Map.txt', 'N10-Reduce.txt',
    'N11-Docker.txt'
]

Ns, bonus = check_and_cap_score(read_score('Ns-Intro.txt'))
bonus_vaje += bonus

Ni, bonus = check_and_cap_score(read_score('Ni-SYCL.txt'))
bonus_vaje += bonus

N00, bonus = check_and_cap_score(read_score('N00-Shell.txt'))
bonus_vaje += bonus

N01, bonus = check_and_cap_score(read_score('N01-Linux-VM.txt'))
bonus_vaje += bonus

N02, bonus = check_and_cap_score(read_score('N02-Linux-Cluster.txt'))
bonus_vaje += bonus

N03, bonus = check_and_cap_score(read_score('N03-MPI-PingPong.txt'))
bonus_vaje += bonus

N04, bonus = check_and_cap_score(read_score('N04-MPI-Cluster.txt'))
bonus_vaje += bonus

N05, bonus = check_and_cap_score(read_score('N05-Sync.txt'))
bonus_vaje += bonus

N06, bonus = check_and_cap_score(read_score('N06-Control.txt'))
bonus_vaje += bonus

N07, bonus = check_and_cap_score(read_score('N07-Hadoop-Single.txt'))
bonus_vaje += bonus

N08, bonus = check_and_cap_score(read_score('N08-Hadoop-Cluster.txt'))
bonus_vaje += bonus

N09, bonus = check_and_cap_score(read_score('N09-Map.txt'))
bonus_vaje += bonus

N10, bonus = check_and_cap_score(read_score('N10-Reduce.txt'))
bonus_vaje += bonus

N11, bonus = check_and_cap_score(read_score('N11-Docker.txt'))
bonus_vaje += bonus

K1 = read_score('K1.txt')
K2 = read_score('K2.txt')

total_points_vaje = (Ns + Ni + N00 + N01 + N02 + N03 + N04 + N05 + N06 + N07 + N08 + N09 + N10 + N11) / 90 * 50
total_points = 0;
    
if K1 < 35 or K2 < 35:
    if Izpit > 50:
        total_points = (Izpit/2) + total_points_vaje
    else:
        total_points = -1
else:
    total_points = (K1 + K2)/4 + total_points_vaje

if total_points > 50:
    total_points = total_points + Bonus + bonus_vaje
    
final_grade = 5
if total_points != -1:
    if total_points >= 50 and total_points <60:
        final_grade = 6
    elif total_points >= 60 and total_points <70:
        final_grade = 7
    elif total_points >= 70 and total_points <80:
        final_grade = 8
    elif total_points >= 80 and total_points <90:
        final_grade = 9
    elif total_points >= 90:
        final_grade = 10
    print(f"Total Points: {total_points}")
    print(f"Final Grade: {final_grade}")
else:
    print(f"You failed!")
    print(f"Final Grade: 5")

assignment_deadline = "2024-10-21"
exam_deadline = "Not yet availabe"
course_name = "RAČUNANJE V OBLAKU"
provider = "FERI, UM"
place_time = "FERI, UM"

print(f"Assignment Defense Deadline: {assignment_deadline}")
print(f"Exam Deadline: {exam_deadline}, Course: {course_name}, Provider: {provider}, Place: {place_time}")





filenames = [
    'Ns-Intro.txt', 'Ni-SYCL.txt', 'N00-Shell.txt', 'N01-Linux-VM.txt', 'N02-Linux-Cluster.txt',
    'N03-MPI-PingPong.txt', 'N04-MPI-Cluster.txt', 'N05-Sync.txt', 'N06-Control.txt', 
    'N07-Hadoop-Single.txt', 'N08-Hadoop-Cluster.txt', 'N09-Map.txt', 'N10-Reduce.txt',
    'N11-Docker.txt', 'K1.txt', 'K2.txt', 'BonusSodelovanje.txt', 'Izpit.txt'
]

for filename in filenames:
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error deleting {filename}: {e}")
