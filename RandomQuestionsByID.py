#Git link:
'''
Eden Dahan 318641222
Ruth Avivi 208981555
Ron Mansharof  208839787
Benny Shalom 203500780

RandomQuestionsByID
'''
RANDOM_MODULUS = 3


def generate_question(questions_set, id, id_questions, num_of_questions=1):
    n = id % len(questions_set)
    res = min(questions_set) + n
    while num_of_questions:
        if res in questions_set:
            id_questions.append(res)
            questions_set.remove(res)
            num_of_questions -= 1
        else:
            if res == max(questions_set):
                res = min(questions_set)
            else:
                res += 1


def random_questions(ids):
    q1 = set(range(1, 10))
    q2 = set(range(10, 19))
    q3 = set(range(10, 19))
    q4 = set(range(19, 31))
    q5 = set(range(19, 31))
    q6 = set(range(31, 37))
    questions = []
    id_questions = []
    #first_id = ids[0]
    i=1
    j=2
    # Generate question 1.
    generate_question(q1, ids[1], id_questions)
    # Generate question 2.
    generate_question(q2, ids[2]-i, id_questions)
    # Generate question 3.
    generate_question(q3, ids[0], id_questions)
    # Generate question 4.
    generate_question(q4, ids[3]-j, id_questions)
    # Generate question 5.
    generate_question(q5, ids[3], id_questions)
    # Generate question 6.
    generate_question(q6, ids[0], id_questions)
    print(id_questions)



ids = [318641222, 208839787, 203500780, 208981555]
print(ids)
ids = sorted(ids, key=lambda my_id: my_id % RANDOM_MODULUS)
print(ids)
random_questions(ids)


