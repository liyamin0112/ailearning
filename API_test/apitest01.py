import requests
API_URL="https://api-inference.huggingface.co/models/uer/gpt2-chinese-cluecorpussmall"

#匿名访问
response = requests.post(API_URL,json={"input":"你好，huggingface"})
print(response.json())