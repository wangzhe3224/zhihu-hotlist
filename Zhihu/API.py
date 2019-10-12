HOST = "https://www.zhihu.com/api"

APIs = {
    "hot-list": {
        "url": "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total",
        "method": "GET",
        "query": [
            "limit"
        ]
    },
    "question": {
        "url": "https://api.zhihu.com/questions/{question_id}",
        "method": "GET",
        "parameters": ['question_id']
    },
    "question2": {
        "url": "https://www.zhihu.com/api/v4/questions/{question_id}}",
        "method": "GET",
        "parameters": ['question_id']
    },
    "question_answers": {
        "url": "https://www.zhihu.com/api/v4/questions/{question_id}/answers",
        "method": "GET",
        "parameters": ["question_id"]
    },
    "answer": {
        "url": "https://www.zhihu.com/api/v4/answers/{answer_id}}",
        "method": "GET",
        "parameters": ["answer_id"]
    },
}