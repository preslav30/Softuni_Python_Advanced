def students_credits(*raw_strings):
    courses = [i.split('-') for i in raw_strings]
    total_credits_received = 0
    credits1 = []
    result = []

    for course in courses:
        course_name, received_points, max_points, max_credits = course[0], float(course[3]), float(course[2]), float(course[1])
        current_credits = (received_points / max_points) * max_credits
        total_credits_received += current_credits
        credits1.append([course_name, current_credits])
    credits_needed = 240 - total_credits_received
    credits1.sort(key=lambda c: c[1], reverse=True)

    if total_credits_received >= 240:
        result.append(f'Diyan gets a diploma with {total_credits_received:.1f} credits.')
    else:
        result.append(f'Diyan needs {credits_needed:.1f} credits more for a diploma.')
    for x, y in credits1:
        result.append(f'{x} - {y:.1f}')
    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

