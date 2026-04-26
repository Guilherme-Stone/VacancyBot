from transformers import pipeline, GenerationConfig
import torch

class JobIA:

    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-1.5B-Instruct",
            device_map="auto",
        )

        self.generation_config = GenerationConfig(
            max_new_tokens=150,
            #do_sample says: create text about this thing
            do_sample=False,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )

    async def search_ia(self, instruction, text):
        response = [{
            "role": "user",
            "content": f"DO {instruction}\n\nWITH:\n{text}"
        }]

        prompt = self.pipe.tokenizer.apply_chat_template(
            response,
            tokenize=False,
            add_generation_prompt=True
        )

        outputs = self.pipe(
            prompt,
            generation_config=self.generation_config,
            return_full_text=False
        )

        generated = outputs[0]["generated_text"]

        if generated.startswith(prompt):
            generated = generated[len(prompt):]

        return generated.strip()