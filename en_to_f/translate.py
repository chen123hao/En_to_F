from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
def translation(input_sequence):
    # input_sequence = "tomorrow is a mystery"
    # input_sequence_3 = "He is pretty kind that I did not expect"
    # input_sequence_4 = "Her eyes are blue"
    task_prefix = "translate English to French: "
    input_sequences = [input_sequence]
    # input_sequences.extend([input_sequence_3, input_sequence_4])

    tokenizer = T5Tokenizer.from_pretrained("t5-base")

    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    #task specific parameter
    encoding = tokenizer([task_prefix + sequence for sequence in input_sequences]
                        , padding = False

                        , return_tensors="pt").input_ids
    outputs = model.generate(encoding)
    result = tokenizer.batch_decode(outputs, skip_special_tokens = True)
    result = result[0]

    return result, outputs

if __name__ == "__main__":
    a = translation("To avoid this warning, please instantiate this tokenizer with `model_max_length` set to your preferred value.")

    print(a[0])
    print(a[1])


