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
            "input": [iter([1, 4]), iter([2, 6]), iter([8, 10]), iter([12, 19])],
            "answer": [[1, 6], [8, 10], [12, 19]]
        },
        {
            "input": [iter([1, 12]), iter([2, 3]), iter([4, 7])],
            "answer": [[1, 12]]
        },
        {
            "input": [iter([1, 5]), iter([6, 10]), iter([10, 15]), iter([17, 20])],
            "answer": [[1, 15], [17, 20]]
        }
    ],
    "Extra": [
        {
            "input": [iter([1, 4]), iter([12, 19])],
            "answer": [[1, 4], [12, 19]]
        },
        {
            "input": [iter([2, 6]), iter([6, 10]), iter([10, 19])],
            "answer": [[2, 19]]
        },
        {
            "input": [iter([2, 6])],
            "answer": [[2, 6]]
        },
        {
            "input": [iter([])],
            "answer": []
        },
        {
            "input": [iter([1, 5]), iter([1, 5])],
            "answer": [[1, 5]]
        },
        {
            "input": [iter([1, 5]), iter([1, 5]), iter([1, 5])],
            "answer": [[1, 5]]
        },
        {
            "input": [iter([2, 16]), iter([3, 5])],
            "answer": [[2, 16]]
        },
        {
            "input": [iter([2, 16]), iter([3, 15]), iter([4, 10])],
            "answer": [[2, 16]]
        },
        {
            "input": [iter([2, 16]), iter([3, 15]), iter([5, 20])],
            "answer": [[2, 20]]
        },
        {
            "input": [iter([2, 16]), iter([3, 3]), iter([3, 3]), iter([16, 16])],
            "answer": [[2, 16]]
        },
        {
            "input": [iter([2, 16]), iter([17, 17])],
            "answer": [[2, 17]]
        }
    ]
}
