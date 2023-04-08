from transformers import AutoTokenizer, MarianMTModel, AutoTokenizer, AutoModelForSeq2SeqLM
from easydict import EasyDict
import yaml

# Read config.yaml file
# with open("config.yaml") as infile:
#     SAVED_CFG = yaml.load(infile, Loader=yaml.FullLoader)
#     CFG = EasyDict(SAVED_CFG["CFG"])
#https://huggingface.co/QuoQA-NLP/KE-T5-En2Ko-Base/tree/main
def translation(src_text,mod
):
    with open(mod + ".yaml") as infile:
        SAVED_CFG = yaml.load(infile, Loader=yaml.FullLoader)
        CFG = EasyDict(SAVED_CFG["CFG"])
    src_text = [src_text]
    # model_name = "/home/ubuntu/En_to_Ko/ke-t5-base-finetuned-en-to-ko/checkpoint-17850"
    model_name = CFG.inference_model_name
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_auth_token=True)

    translated = model.generate(
        **tokenizer(src_text, return_tensors="pt", padding=True, max_length=CFG.max_token_length,),
        max_length=CFG.max_token_length,
        num_beams=CFG.num_beams,
        repetition_penalty=CFG.repetition_penalty,
        no_repeat_ngram_size=CFG.no_repeat_ngram_size,
        num_return_sequences=CFG.num_return_sequences,
    )
    result = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return  result[0]
if __name__ == "__main__":
    a = translation("Évidemment, le problème du noircissement dans les scènes nocturnes est plus difficile.",mod="config2")
    print(a)