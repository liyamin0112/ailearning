from transformers import BertTokenizer,BertForSequenceClassification,pipeline
model_name ="bert-base-chinese"
cache_dir = "model/bert-base-chinese"
model =BertForSequenceClassification.from_pretrained(model_name,cache_dir=cache_dir)
tokenizer= BertTokenizer.from_pretrained(model_name,cache_dir=cache_dir)
print(f"{model_name}download:{cache_dir}")
classifier = pipeline("text-classification",model=model,tokenizer=tokenizer,device="cuda")
result = classifier("你好，我是一款语言模型")
print(result)