from openai.types.chat import ChatCompletion
from unittest.mock import Mock


# Create a mock object
openai_api_mock = Mock()

# Define what the .chat.completions.create method should return
openai_api_mock.chat.completions.create.return_value = ChatCompletion(
    id="chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
    model="gpt-3.5-turbo-0613",
    object="chat.completion",
    created=1677664795,
    choices=[
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                        "content": "This repository is for a project called \"GitHub Repository Comparer.\" The purpose of this project is to compare two GitHub repositories and display the differences between them. It provides a web interface where users can enter the URLs of two repositories, and the system will retrieve the necessary information from the GitHub API. This information includes the number of stars, forks, pull requests, issues, and commits, as well as details about the top contributors for each repository. The comparison results are then displayed, allowing users to easily see the differences between the two repositories.",
                        "role": "assistant"
                },
            "logprobs": None,
        }
    ],
)