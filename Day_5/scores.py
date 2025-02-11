student_scores = [180, 124, 165, 173, 189, 169, 146]

print(f"Built in {max(student_scores)}")

my_max = 0
for score in student_scores:
    if score > my_max:
        my_max = score

print(f"My max {my_max}")
