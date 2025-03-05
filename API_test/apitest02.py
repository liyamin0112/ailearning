from transformers import AutoModelForCausalLM,AutoTokenizer
model_name ="uer/gpt2-chinese-cluecorpussmall"
cache_dir = "model/uer/gpt2-chinese-cluecorpussmall"
AutoModelForCausalLM.from_pretrained(model_name,cache_dir=cache_dir)
AutoTokenizer.from_pretrained(model_name,cache_dir=cache_dir)
print(f"download:{cache_dir}")
