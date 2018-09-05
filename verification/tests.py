"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(1, 4), (2, 6), (8, 10), (12, 19)],
            "answer": [[1, 6], [8, 10], [12, 19]]
        },
        {
            "input": [(1, 12), (2, 3), (4, 7)],
            "answer": [[1, 12]]
        },
        {
            "input": [(1, 5), (6, 10), (10, 15), (17, 20)],
            "answer": [[1, 15], [17, 20]]
        }
    ],
    "Extra": [
        {
            "input": [(1, 4), (12, 19)],
            "answer": [[1, 4], [12, 19]]
        },
        {
            "input": [(2, 6), (6, 10), (10, 19)],
            "answer": [[2, 19]]
        },
        {
            "input": [(2, 6)],
            "answer": [[2, 6]]
        },
        {
            "input": [],
            "answer": []
        },
        {
            "input": [(1, 5), (1, 5)],
            "answer": [[1, 5]]
        },
        {
            "input": [(1, 5), (1, 5), (1, 5)],
            "answer": [[1, 5]]
        },
        {
            "input": [(2, 16), (3, 5)],
            "answer": [[2, 16]]
        },
        {
            "input": [(2, 16), (3, 15), (4, 10)],
            "answer": [[2, 16]]
        },
        {
            "input": [(2, 16), (3, 15), (5, 20)],
            "answer": [[2, 20]]
        },
        {
            "input": [(2, 16), (3, 3), (3, 3), (16, 16)],
            "answer": [[2, 16]]
        },
        {
            "input": [(2, 16), (17, 17)],
            "answer": [[2, 17]]
        }
    ]
}
