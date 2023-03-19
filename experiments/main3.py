import onnx
import random
import torch
import string
import transformers
import numpy as np
import onnxruntime as ort
from pathlib import Path
from unidecode import unidecode
from functools import cache
from nltk.corpus import stopwords
from torch.nn.functional import cosine_similarity
from transformers import AutoTokenizer, AutoModel, BartModel, BertModel
from transformers.onnx import FeaturesManager
from numpy import dot
from numpy.linalg import norm

english_stopwords = stopwords.words("english")
model = AutoModel.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

model_kind, model_onnx_config = FeaturesManager.check_supported_model_or_raise(model)
onnx_config = model_onnx_config(model.config)

onnx_inputs, onnx_outputs = transformers.onnx.export(
    preprocessor=tokenizer,
    model=model,
    config=onnx_config,
    opset=13,
    output=Path("onnx/model.onnx"),
)

ort_sess = ort.InferenceSession("onnx/model.onnx")

resume = {
    ("name", "full name"): ["Peter Jung"],
    ("job title", "job", "title"): ["Senior Machine Learning Engineer"],
    ("location", "city", "state", "republic"): ["Prague, Czech Republic"],
    ("occupation", "company", "work"): [
        "Senior Machine Learning Engineer at leadiQ, San Francisco Bay Area"
    ],
    ("years of experience",): ["6+ years"],
    ("doctorate", "phd"): [
        "Part-timt student of PhD in Artificial Intelligence, however works full-time as a Senior Machine Learning Engineer without any interventions with work-time."
    ],
    ("github", "project", "projects", "github projects", "repository"): [
        "https://github.com/kongzii/"
        "On Discovering Interesting Combinatorial Integer Sequences: https://arxiv.org/abs/2302.04606v1"
        "Using Machine Learning to Detect if Two Products Are the Same: https://dspace.cvut.cz/handle/10467/87875?locale-attribute=en"
    ],
    ("experience", "work experience"): [
        "Creating GPT-based sales email writer with human-beating quality.",
        "Created prompts to get desired behaviour from pretrained one/few shot models.",
        "Increased the accuracy of the multilingual sentiment analysis model written in PyTorch by 21%.",
        "Created a multi-modal (image and text input) model written in TensorFlow that reduces the workload of the other team by 84%.",
        "Optimized existing models to have more than 50% faster inference speed and lower memory usage.",
        "Delivered machine learning infrastructure based on Terraform (Terragrunt) infrastructure as code (IaC) on AWS.",
        "Configured AWS EKS (Kubernetes) with EC2 and Fargate workers.",
        "Deployed MLflow and Airflow to Kubernetes, including KEDA auto-scaling, XComs stored in S3, and workers configured for Fargate and EC2.",
        "Wrote case studies and blog posts about the whole process and outcome, available at https://pilotcoresystems.com/insights/.",
        "Designed the architecture of the whole system, including the NLP and boosted trees model, for automatic product pairing, using Kafka for message streaming, Docker for deployment in Kubernetes, PyTorch and TensorFlow as deep learning frameworks.",
        "Redesigned and developed the core of the main back-end microservice, serving thousands of requests per second faster, migrated from Flask to FastAPI, serving data from MySQL.",
        "Introduced Apache Kafka for real-time data streaming.",
        "Built back-end and front-end components for marketing and reporting system for the BMW, GGTabak and other big companies.",
    ],
    (
        "education",
        "school",
        "degree",
        "university",
    ): [
        "Master's degree, Artificial Intelligence, Czech Technical University",
        "Bachelor's degree, Automotive Mechatronics, University of Technology Bratislava",
    ],
    ("skills",): [
        "Software Development 6+ years",
        "Python 5+ years",
        "Machine Learning 4+ years",
        "AWS 2+ years",
        "MLOps 1+ year",
    ],
}


def cosine_similarity_numpy(a, b):
    return dot(a, b) / (norm(a) * norm(b))


@cache
def encode(text):
    encoded_input = tokenizer(text, return_tensors="pt")
    output = ort_sess.run(
        None,
        {
            "input_ids": encoded_input.input_ids.numpy(),
            "token_type_ids": encoded_input.token_type_ids.numpy(),
            "attention_mask": encoded_input.attention_mask.numpy(),
        },
    )
    state = np.mean(output[0], axis=1).squeeze()
    return state


@cache
def preprocess_question(text):
    text = text.lower()
    text = text.replace("peter", "")
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(word for word in text.split() if word not in english_stopwords)
    text = unidecode(text)
    return text


def answer(question):
    question_processed = preprocess_question(question)
    question_encoded = encode(question_processed)

    best_sim = float("-inf")
    values_candidates = []

    for keys, values in resume.items():
        for key in keys:
            key_encoded = encode(key)
            similarity = cosine_similarity_numpy(question_encoded, key_encoded).item()
            if similarity > best_sim:
                best_sim = similarity
                values_candidates = values

    values_candidates = sorted(
        values_candidates,
        key=lambda x: cosine_similarity_numpy(encode(x), question_encoded),
        reverse=True,
    )
    n = random.randint(min(3, len(values_candidates)), len(values_candidates))
    values = values_candidates[:n]

    return values


while True:
    question = input("what's your question? ") or "what is his education?"
    print(answer(question))
