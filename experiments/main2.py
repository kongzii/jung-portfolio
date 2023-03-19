import onnx
import torch
import onnxruntime as ort
from pprint import pprint
from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
)


model = AutoModelForQuestionAnswering.from_pretrained(
    "bert-large-uncased-whole-word-masking-finetuned-squad"
)
tokenizer = AutoTokenizer.from_pretrained(
    "bert-large-uncased-whole-word-masking-finetuned-squad"
)

model.save_pretrained("local-pt-checkpoint-2")
tokenizer.save_pretrained("local-pt-checkpoint-2")

context = """
    Name: Peter Jung
    Job Title: Senior Machine Learning Engineer
    Location: Prague, Czech Republic
EXPERIENCE
    Senior Machine Learning Engineer at leadiQ, San Francisco Bay Area
        Creating GPT-based sales email writer with human-beating quality.
        Created prompts to get desired behaviour from pretrained one/few shot models.
    Researcher at Emplifi Inc., Prague, CZ
        Increased the accuracy of the multilingual sentiment analysis model written in PyTorch by 21%.
        Created a multi-modal (image and text input) model written in TensorFlow that reduces the workload of the other team by 84%.
        Optimized existing models to have more than 50% faster inference speed and lower memory usage.
    MLOps at Pilotcore Systems Inc., Toronto, CA
        Delivered machine learning infrastructure based on Terraform (Terragrunt) infrastructure as code (IaC) on AWS.
        Configured AWS EKS (Kubernetes) with EC2 and Fargate workers.
        Deployed MLflow and Airflow to Kubernetes, including KEDA auto-scaling, XComs stored in S3, and workers configured for Fargate and EC2.
        Wrote case studies and blog posts about the whole process and outcome, available at https://pilotcoresystems.com/insights/.
    Software & Machine Learning at Heureka Group, a.s., Prague, CZ
        Designed the architecture of the whole system, including the NLP and boosted trees model, for automatic product pairing, using Kafka for message streaming, Docker for deployment in Kubernetes, PyTorch and TensorFlow as deep learning frameworks.
        Redesigned and developed the core of the main back-end microservice, serving thousands of requests per second faster, migrated from Flask to FastAPI, serving data from MySQL.
        Introduced Apache Kafka for real-time data streaming.
    Full Stack Developer at M7, s.r.o., Bratislava, SK
        Built back-end and front-end components for marketing and reporting system for the BMW, GGTabak and other big companies.
EDUCATION
    Master's degree
        Artificial Intelligence
        Czech Technical University
        2018 - 2020
    Bachelor's degree
        Automotive Mechatronics
        University of Technology
        2015 - 2018
SKILLS
    Software Development: 6+ years
    Python: 5+ years
    Machine Learning: 4+ years
    AWS: 2+ years
    MLOps: 1+ year
"""
question = "How many years of experience?"

inputs = tokenizer(question, context, return_tensors="pt")

print(inputs.input_ids.shape)
with torch.no_grad():
    outputs = model(**inputs)

answer_start_index = int(torch.argmax(outputs.start_logits, dim=-1)[0])
answer_end_index = int(torch.argmax(outputs.end_logits, dim=-1)[0])

predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
print("here")
print(tokenizer.decode(predict_answer_tokens))
