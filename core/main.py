from core import client, MODEL

def get_response(project_link, prompt):
  # more message needed
  response = client.chat.completions.create(
      model=MODEL,
      messages=[
      {"role": "system", "content": f"You are a knowledgeable member of the GitHub repository at {project_link}. You are familiar with all the details and the purpose of the project."},
      {"role": "user", "content": f"{prompt}"},
    ]
  )
  return response

if __name__ == "__main__":
  response = get_response("https://github.com/wxharry/github-repo-comparer/", "What does this repository do?")
  print(response.choices[0].message.content)

