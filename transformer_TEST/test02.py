from openpyxl.styles.builtins import output
from transformers import AutoModelForCausalLM,AutoTokenizer,pipeline

#设置模型路径 config.json的目录,只支持绝对路径r:fang转义字符
model_dir = r"G:\code\Hugging_face_learning\API_test\model\uer\gpt2-chinese-cluecorpussmall\models--uer--gpt2-chinese-cluecorpussmall\snapshots\c2c0249d8a2731f269414cc3b22dff021f8e07a3"
model =AutoModelForCausalLM.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)
#生成文本pipline

generator = pipeline("text-generation",model=model,tokenizer=tokenizer,device="cuda")
output = generator("春天，",max_length= 50,num_return_sequences=1)
print(output)