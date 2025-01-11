def enrollment_stats(universities):
    enrollment_values, tuition_fees = [], []
    for university in universities:
        enrollment_values.append(university[1])
        tuition_fees.append(university[2])
    return enrollment_values, tuition_fees


def mean(a):
    return sum(a) / len(a)


def median(a):
    return sorted(a)[len(a) // 2]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

print(f"******************************\nTotal students: {sum(enrollment_stats(universities)[0])}\n"
      f"Total tuition: {sum(enrollment_stats(universities)[1])}\n\nStudent mean: {round(mean(enrollment_stats(universities)[0]), 2)}\n"
      f"Student median: {median(enrollment_stats(universities)[0])}\n\nTuition mean: & {round(mean(enrollment_stats(universities)[1]), 2)}\n"
      f"Tuition median: & {median(enrollment_stats(universities)[1])}\n******************************")
