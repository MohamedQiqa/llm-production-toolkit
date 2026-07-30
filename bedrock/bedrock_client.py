import os
import boto3
import json
from dotenv import load_dotenv
from transformers import AutoTokenizer

load_dotenv(override=True)
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.environ.get("AWS_SESSION_TOKEN")
MODEL_ARN = os.environ.get("MODEL_ARN")

tokenizer = AutoTokenizer.from_pretrained("MohamedQiqa/Llama-3.2-1B-QLoRA-Summarizer")

bedrock = boto3.client(
    "bedrock-runtime",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
)

dialogue = "Victoria: God I'm really broke, I spent way to much this month \nVictoria: At least we get paid soon..\nMagda: Yeah, don't remind me, I know the feeling\nMagda: I just paid my car insurance, I feel robbed \nVictoria: Thankfully mine is paid for the rest of the year"

prompt = f"Summarize this dialogue:\n{dialogue}"

prompt_template = tokenizer.apply_chat_template(
    [
        {
            "role": "system",
            "content": "You are a helpful assistant that summarizes dialogues.",
        },
        {"role": "user", "content": prompt},
    ],
    tokenize=False,
)

response = bedrock.invoke_model(
    modelId=MODEL_ARN,
    contentType="application/json",
    body=json.dumps(
        {
            "prompt": prompt_template,
            "max_tokens": 200,
            "temperature": 0.01,
        }
    ),
)

result = json.loads(response["body"].read())
print(result["choices"][0]["text"])
