from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")

# onnx_model = onnx.load("onnx/model.onnx")
# onnx.checker.check_model(onnx_model)


context = """
RESUME

    Name: Peter Jung
    Job Title: Senior Machine Learning Engineer
    Location: Prague, Czech Republic

EXPERIENCE

    Senior Machine Learning Engineer at leadiQ, San Francisco Bay Area
        November 2022 - current (full-time, contract-based)
        Creating GPT-based sales email writer with human-beating quality.
        Created prompts to get desired behaviour from pretrained one/few shot models.
        Deployed APIs in production.
    Researcher at Emplifi Inc., Prague, CZ
        November 2020 - November 2022
        Increased the accuracy of the multilingual sentiment analysis model written in PyTorch by 21%.
        Created a multi-modal (image and text input) model written in TensorFlow that reduces the workload of the other team by 84%.
        Optimized existing models to have more than 50% faster inference speed and lower memory usage.
        Implemented a reverse image and video search engine with PyTorch and FAISS.
        Created an extreme text classification system with APIs for training and inference management, with an automatic training pipeline in Databricks.
        Assured that experiments are fully reproducible by properly using tools like MLflow, Git, DVC, Docker, and others.
        Started Python educational group.
    MLOps at Pilotcore Systems Inc., Toronto, CA
        March 2022 - June 2022 (part-time, contract-based)
        Delivered machine learning infrastructure based on Terraform (Terragrunt) infrastructure as code (IaC) on AWS.
        Configured AWS EKS (Kubernetes) with EC2 and Fargate workers.
        Deployed MLflow and Airflow to Kubernetes, including KEDA auto-scaling, XComs stored in S3, and workers configured for Fargate and EC2.
        Wrote case studies and blog posts about the whole process and outcome, available at https://pilotcoresystems.com/insights/.
    Software & Machine Learning at Heureka Group, a.s., Prague, CZ
        July 2019 - October 2020
        Designed the architecture of the whole system, including the NLP and boosted trees model, for automatic product pairing, using Kafka for message streaming, Docker for deployment in Kubernetes, PyTorch and TensorFlow as deep learning frameworks.
        Redesigned and developed the core of the main back-end microservice, serving thousands of requests per second faster, migrated from Flask to FastAPI, serving data from MySQL.
        Introduced Apache Kafka for real-time data streaming.
    Full Stack Developer at M7, s.r.o., Bratislava, SK
        July 2017 - July 2019
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

LANGUAGES

    English, Czech, Slovak: Fully communicative

ACHIEVEMENTS

    MLPrague Speaker: Biggest European ML conference.
    Top 1% Developer: Accepted at Turing, Gun.io, Adevait and others.
"""

while True:
    question = input("Question: ")

    prompt = f"""Resume:
    {context}
    Question:
    {question}
    Answer:
    """
    prompt_tokenized = tokenizer(prompt, return_tensors="pt")
    gen_tokens = model.generate(
        prompt_tokenized.input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=2048,
        early_stopping=True,
    )
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    print(gen_text)
