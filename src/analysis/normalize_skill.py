ALIASES = {
    # Core AI / ML
    "ml": "machine learning",
    "machine learning": "machine learning",
    "dl": "deep learning",
    "deep learning": "deep learning",
    "ai": "artificial intelligence",
    "artificial intelligence": "artificial intelligence",

    # NLP
    "nlp": "nlp",
    "natural language processing": "nlp",
    "text classification": "nlp",
    "ner": "nlp",
    "named entity recognition": "nlp",
    "sentiment analysis": "nlp",
    "word embeddings": "nlp",
    "transformers": "nlp",
    "language modeling": "nlp",
    "chatbots": "nlp",

    # Computer Vision
    "cv": "computer vision",
    "computer vision": "computer vision",
    "cnn": "cnn",
    "convolutional neural network": "cnn",
    "rnn": "rnn",
    "recurrent neural network": "rnn",
    "lstm": "lstm",
    "long short term memory": "lstm",
    "gan": "gan",
    "generative adversarial network": "gan",
    "autoencoder": "autoencoder",
    "image classification": "computer vision",
    "object detection": "computer vision",
    "image segmentation": "computer vision",
    "face recognition": "computer vision",
    "ocr": "computer vision",

    # Programming
    "python": "python",
    "r": "r",
    "java": "java",
    "c": "c",
    "c++": "c++",
    "c#": "c#",
    "js": "javascript",
    "javascript": "javascript",
    "bash": "bash/shell scripting",
    "shell": "bash/shell scripting",

    # Libraries & Frameworks
    "tensorflow": "tensorflow",
    "keras": "keras",
    "pytorch": "pytorch",
    "scikit-learn": "scikit-learn",
    "sklearn": "scikit-learn",
    "opencv": "opencv",
    "nltk": "nltk",
    "spacy": "spacy",
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "huggingface": "huggingface transformers",
    "transformers library": "huggingface transformers",

    # Data & Databases
    "data analysis": "data analysis",
    "eda": "data analysis",
    "data science": "data science",
    "sql": "sql",
    "mysql": "mysql",
    "postgresql": "postgresql",
    "mongodb": "mongodb",
    "nosql": "nosql",

    # Cloud / DevOps / MLOps
    "aws": "aws",
    "gcp": "gcp",
    "azure": "azure",
    "docker": "docker",
    "kubernetes": "kubernetes",
    "ci/cd": "ci/cd",
    "mlops": "mlops",
    "continuous integration": "mlops",
    "continuous deployment": "mlops",
    "model versioning": "mlops",
    "data versioning": "mlops",
    "experiment tracking": "mlops",
    "pipeline automation": "mlops",
    "model monitoring": "mlops",
    "model retraining automation": "mlops",
    "feature store": "mlops"
}

def normalize_skill(skills):
    return sorted({
        ALIASES.get(skill.lower(), skill.lower())
        for skill in skills
    })
