import requests
import json

# def len_joke():
#   joke = get_joke()
#   return len(joke)

def get_quote():
  url = 'https://dummyjson.com/quotes'
  response = requests.get(url)
  response_json = json.loads(response.text)
  #print(type(response_json))  #<class 'dict'>

  #Get the quote title for the 1st quote in the response
  quote = response_json['quotes'][0]['quote']
  print(quote)

  # for key in response_json:
  #   print(key)
  #print(dir(response))
  #print(response_json['quotes'][0])
  
  # if response.status_code == 200:
  #   quote = response.json()['quotes'][0]['quote']
  #   #print(quote)
  # else:
  #   quote = 'No quotes'
  
  # return quote

def getPosts():
  url = 'https://jsonplaceholder.typicode.com/posts'
  response = requests.get(url)
  response_json = json.loads(response.text)
  #posts = json.loads(response.text)
  print(type(response_json))  #<class 'list'>
  return response_json

def getPosts():
  url = 'https://jsonplaceholder.typicode.com/posts'
  response = requests.get(url)
  #response_json = json.loads(response.text)
  posts = json.loads(response.text)
  #print(type(response_json))  #<class 'list'>
  #for post in posts:
  #  if post['id'] == 2:
      #print(f"type for post: {type(post)}")
      #print(post['title'])
  #print(f"End of getPosts()")
  return posts

def getPostsUsingQueryParam():
  # Passing Query param in the url. Method 1
  # url = 'https://dummyjson.com/posts?skip=3&limit=2'
  # response = requests.get(url)
  # Either invoke the api using the full url with query param as shown above or use it as follows:
  url = 'https://dummyjson.com/posts'
  payload = {'skip': 3, 'limit': 2}
  response = requests.get(url, params=payload, )
  # Convert response into Python object (Dictionary/List)
  #response_json = json.loads(response.text)
  response_json = response.json()
  print(f"Type of response: {type(response_json)}")
  print(response_json)

  """
  If you want to see the response printed on terminal in pretty format, then you need to convert the
  python object to a valid json using dumps() method and then when you run the program via terminal, then run 
  using following command
  python main_v2.py | python -m json.tool
  """
  #print(json.dumps(response_json)) # this will convert a python object to a valid json

  


if __name__ == '__main__':
  getPostsUsingQueryParam()
  #pass
  #print(get_quote())
  #print(getPosts())
