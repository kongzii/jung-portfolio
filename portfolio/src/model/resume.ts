/*
    This file contains the resume data.
    Question-answering model will embed the question and look for the most similar answer based on the phrases below and answer the assigned response.

    The format is as follows:
    [
        [
            ["question1", "question2", "question3"], // All questions that are closests to one of these phrases will be assigned the same response
            ["answer", "potentionally", "over", "multiple", "lines"]  // Each item will be written on a new line
        ],
    ]
*/
export const resumeArrayish = [
    [["hello", "hi", "hey", "whats up", "good morning", "good day"], ["Hello!"]],
    [["name", "full name"], ["Peter Jung"]],
    [["job title", "job", "title", "current job"], ["Senior Machine Learning Engineer"]],
    [["location", "city", "state", "republic", "live in", "lives in", "live", "lives"], [
        "Although he resides in Prague, Czech Republic, he has gained professional experience by working for companies located in the USA, Canada, Singapore, and Slovakia.",
        "",
        "Therefore, he has a proven record of adapting to just any timezone.",
    ]],
    [["occupation", "company", "work", "employer", "specialization"], [
        `<b>Senior Machine Learning Engineer</b> at <a href="https://leadiq.com/">leadiQ</a>, San Francisco Bay Area`
    ]],
    [["doctorate", "phd", "studium"], [
        "Part-time student of PhD in Artificial Intelligence, however works full-time as a Senior Machine Learning Engineer without any interventions with his work-time."
    ]],
    [["linkedin", "linkedin profile", "linkedin link", "linkedin.com"], [
        `<a href="https://www.linkedin.com/in/jung-ninja/" target="_blank">https://www.linkedin.com/in/jung-ninja/</a>`,
    ]],
    [["github", "project", "projects", "github projects", "repository", "open source", "open-source", "c++", "python", "swift", "graph", "arxiv"], [
        `Contributor of the following open-source libraries:<br/>`,
        ` • <a href="https://github.com/pytorch/pytorch" target="_blank">PyTorch - Deep Learning Framework</a>`,
        ` • <a href="https://github.com/huggingface/transformers" target="_blank">Transformers: State-of-the-art Machine Learning</a>`,
        ` • <a href="https://github.com/tensorflow/swift-models" target="_blank">TensorFlow Swift Models</a>`,
        ` • <a href="https://github.com/kayak/pypika" target="_blank">PyPika - Python Query Builder</a>`,
        `<br/>Author of the following libraries:<br/>`,
        ` • <a href="https://github.com/kongzii/mlflow-kubernetes" target="_blank">MLflow deployment for Kubernetes</a>`,
        ` • <a href="https://github.com/kongzii/GraphCpp" target="_blank">Graph library for C++</a>`,
        ` • <a href="https://github.com/kongzii/SwiftXGBoost" target="_blank">XGBoost machine learning framework for Swift</a>`,
        ` • <a href="https://github.com/kongzii/SGSL" target="_blank">Scientific library for Swift</a>`,
        ` • <a href="https://github.com/kongzii/xiaomi-yi-py" target="_blank">Control your Xiamo Yi action camera from your computer</a>`,
        ` • <a href="https://github.com/kongzii/NFA" target="_blank">Full nondeterministic finite automaton implementation in C++</a>`,
        `<br/>Scientific publications:<br/>`,
        ` • <a href="https://arxiv.org/abs/2302.04606v1" target="_blank">On Discovering Interesting Combinatorial Integer Sequences</a>`,
        ` • <a href="https://github.com/kongzii/gangraphon" target="_blank">Graph Generation with Graphon Generative Adversarial Networks</a>`,
        ` • <a href="https://dspace.cvut.cz/handle/10467/87875?locale-attribute=en" target="_blank">Using Machine Learning to Detect if Two Products Are the Same</a>`,
        `<br/>Look for more at <a href="https://github.com/kongzii/" target="_blank">https://github.com/kongzii/</a>! :)`,
    ]],
    [["publications", "papers", "scientific publications", "scientific papers", "research papers"], [
        `<br/>Scientific publications:<br/>`,
        ` • <a href="https://arxiv.org/abs/2302.04606v1" target="_blank">On Discovering Interesting Combinatorial Integer Sequences</a>`,
        ` • <a href="https://github.com/kongzii/gangraphon" target="_blank">Graph Generation with Graphon Generative Adversarial Networks</a>`,
        ` • <a href="https://dspace.cvut.cz/handle/10467/87875?locale-attribute=en" target="_blank">Using Machine Learning to Detect if Two Products Are the Same</a>`,
    ]],
    [["leadiq", "responsibility at leadiq", "work at leadiq", "leadiq.com"], [
        `<a href="https://leadiq.com/" target="_blank">Senior Machine Learning Engineer at leadiQ, San Francisco Bay Area</a><br/>`,

        `• Deployed models on Databricks' serverless model endpoints.`,
        `• Fine-tuned and served GPT3 models.`,
        `• Creating GPT-based sales email writer with human-beating quality.`,
        `• Created prompts to get desired behaviour from pretrained one/few shot models.`,
    ]],
    [["responsibility at emplifi", "work at emplifi", "emplifi", "emplifi.io", "socialbakers"], [
        `<a href="https://emplifi.io/" target="_blank">Researcher at Emplifi Inc., Prague, CZ</a><br/>`,

        `• Increased the accuracy of the multilingual sentiment analysis model written in PyTorch by 21%.`,
        `• Created a multi-modal (image and text input) model written in TensorFlow that reduces the workload of the other team by 84%.`,
        `• Optimized existing models to have more than 50% faster inference speed and lower memory usage.`,
        `• Implemented a reverse image and video search engine with PyTorch and FAISS.`,
        `• Created an extreme text classification system with APIs for training and inference management, with an automatic training pipeline in Databricks.`,
        `• Assured that experiments are fully reproducible by properly using tools like MLflow, Git, DVC, Docker, and others.`,
        `• Started Python educational group.`,
    ]],
    [["pilotcore", "responsibility at pilotcore", "work at pilotcore", "mlops"], [
        `<a href="https://pilotcoresystems.com/" target="_blank">MLOps at Pilotcore Systems Inc., Toronto, CA</a><br/>`,

        `• Delivered machine learning infrastructure based on Terraform (Terragrunt) infrastructure as code (IaC) on AWS.`,
        `• Configured AWS EKS (Kubernetes) with EC2 and Fargate workers.`,
        `• Deployed MLflow and Airflow to Kubernetes, including KEDA auto-scaling, XComs stored in S3, and workers configured for Fargate and EC2.`,
        `• Wrote case studies and blog posts about the whole process and outcome, available at <a href="https://pilotcoresystems.com/insights/" target="_blank">https://pilotcoresystems.com/insights/</a>.`,
    ]],
    [["heureka", "heureka.cz", "heureka.sk", "responsibility at heureka", "work at heureka", "backend"], [
        `<a href="https://www.heureka.cz/" target="_blank">Software & Machine Learning at Heureka Group, a.s., Prague, CZ</a><br/>`,

        `• Designed the architecture of the whole system, including the NLP and boosted trees model, for automatic product pairing, using Kafka for message streaming, Docker for deployment in Kubernetes, PyTorch and TensorFlow as deep learning frameworks.`,
        `• Redesigned and developed the core of the main back-end microservice, serving thousands of requests per second faster, migrated from Flask to FastAPI, serving data from MySQL.`,
        `• Introduced Apache Kafka for real-time data streaming.`,
    ]],
    [["m7", "m7.sk", "fullstack", "frontend", "responsibility at m7", "work at m7"], [
        `<a href="https://m7.sk/" target="_blank">Full Stack Developer at M7, s.r.o., Bratislava, SK</a><br/>`,

        `• Built back-end and front-end components for marketing and reporting system for the BMW, GGTabak and other big companies.`,
    ]],
    [["experience", "work experience", "worked on", "work contributions"], [
        `<a href="https://leadiq.com/" target="_blank">Senior Machine Learning Engineer at leadiQ, San Francisco Bay Area</a><br/>`,

        `• Creating GPT-based sales email writer with human-beating quality.`,
        `• Created prompts to get desired behaviour from pretrained one/few shot models.`,

        `<br/><a href="https://emplifi.io/" target="_blank">Researcher at Emplifi Inc., Prague, CZ</a><br/>`,

        `• Increased the accuracy of the multilingual sentiment analysis model written in PyTorch by 21%.`,
        `• Created a multi-modal (image and text input) model written in TensorFlow that reduces the workload of the other team by 84%.`,
        `• Optimized existing models to have more than 50% faster inference speed and lower memory usage.`,

        `<br/><a href="https://pilotcoresystems.com/" target="_blank">MLOps at Pilotcore Systems Inc., Toronto, CA</a><br/>`,

        `• Delivered machine learning infrastructure based on Terraform (Terragrunt) infrastructure as code (IaC) on AWS.`,
        `• Configured AWS EKS (Kubernetes) with EC2 and Fargate workers.`,
        `• Deployed MLflow and Airflow to Kubernetes, including KEDA auto-scaling, XComs stored in S3, and workers configured for Fargate and EC2.`,
        `• Wrote case studies and blog posts about the whole process and outcome, available at <a href="https://pilotcoresystems.com/insights/" target="_blank">https://pilotcoresystems.com/insights/</a>.`,

        `<br/><a href="https://www.heureka.cz/" target="_blank">Software & Machine Learning at Heureka Group, a.s., Prague, CZ</a><br/>`,

        `• Designed the architecture of the whole system, including the NLP and boosted trees model, for automatic product pairing, using Kafka for message streaming, Docker for deployment in Kubernetes, PyTorch and TensorFlow as deep learning frameworks.`,
        `• Redesigned and developed the core of the main back-end microservice, serving thousands of requests per second faster, migrated from Flask to FastAPI, serving data from MySQL.`,
        `• Introduced Apache Kafka for real-time data streaming.`,

        `<br/><a href="https://m7.sk/" target="_blank">Full Stack Developer at M7, s.r.o., Bratislava, SK</a><br/>`,

        `• Built back-end and front-end components for marketing and reporting system for the BMW, GGTabak and other big companies.`,
    ]],
    [["education", "degree", "university", "school"], [
        `• <b>Master's degree</b>: <a href="https://fel.cvut.cz/en" target="_blank">Artificial Intelligence, Czech Technical University</a>`,
        `• <b>Bachelor's degree</b>: <a href="https://www.fei.stuba.sk/english.html" target="_blank">Automotive Mechatronics, University of Technology Bratislava</a>`,
    ]],
    [["skills", "years of experience", "specializations"], [
        "• Software Development 6+ years",
        "• Python 5+ years",
        "• Machine Learning 4+ years",
        "• AWS 2+ years",
        "• MLOps 1+ year",
    ]],
    [["stack", "tech stack", "tech", "technology", "technologies", "libraries", "docker", "kubernetes", "mlflow", "openai", "transformers"], [
        "• Python - Primary programming language",
        "• PyTorch, TensorFlow - Deep Learning Frameworks",
        "• Transformers, Timm - For pretrained models and model zoo",
        "• OpenAI - Prompt engineering and fine-tuning of LLMs",
        "• Docker, Kubernetes, Terraform, Terragrunt - Deployment and reproducibility",
        "• MLFlow, Neptune.ai, Tensorboard - Experiment tracking and visualization",
        "• Kafka - For real-time data streaming",
        "• Spark, Databricks - For large-scale data processing",
        "• FastAPI, Flask, GraphQL - For back-end development",
        "• Mypy - Type checking for Python",
        "• Vue.js - When in need of a front-end",
    ]],
    [["age", "how old", "date of birth"], [
        "Sorry, this information is not available.",
    ]],
    [["how are you", "how are you doing", "how are you feeling", "how are you doing today", "how are you feeling today", "how you doin"], [
        "Good, thank you!",
    ]],
    [["who are you", "what is your name", "what's your name"], [
        "I'm a resume bot called ninja.",
    ]],
]
