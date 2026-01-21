SKILL_ONTOLOGY = {
    # ===== Core AI / ML =====
    "artificial intelligence": {
        "machine learning",
        "knowledge representation",
        "expert systems",
        "search algorithms",
        "planning",
        "reasoning"
    },

    "machine learning": {
        "supervised learning",
        "unsupervised learning",
        "reinforcement learning",
        "deep learning",
        "nlp",
        "computer vision",
        "ensemble methods",
        "time series analysis",
        "anomaly detection",
        "recommendation systems"
    },

    "deep learning": {
        "neural networks",
        "cnn",
        "rnn",
        "lstm",
        "transformers",
        "autoencoders",
        "gan"
    },

    "nlp": {
        "tokenization",
        "text classification",
        "named entity recognition",
        "sentiment analysis",
        "language modeling",
        "question answering",
        "chatbots",
        "topic modeling",
        "word embeddings"
    },

    "computer vision": {
        "image classification",
        "object detection",
        "image segmentation",
        "face recognition",
        "ocr",
        "image augmentation",
        "video analysis"
    },

    # ===== Programming =====
    "programming": {
        "python",
        "r",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "bash/shell scripting"
    },

    "python": {
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "keras",
        "opencv",
        "nltk",
        "spacy",
        "huggingface transformers",
        "Transformers"
    },

    "javascript": {
        "node.js",
        "react",
        "express"
    },

    # ===== Data =====
    "data analysis": {
        "data cleaning",
        "exploratory data analysis",
        "data visualization",
        "feature engineering",
        "feature selection",
        "dimensionality reduction"
    },

    "data science": {
        "data analysis",
        "machine learning",
        "statistics",
        "probability",
        "bayesian methods"
    },

    # ===== Databases =====
    "databases": {
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "nosql",
        "big data tools"
    },

    # ===== Cloud / DevOps / MLOps =====
    "cloud": {
        "aws",
        "azure",
        "gcp",
        "cloud ml services"
    },

    "devops": {
        "docker",
        "kubernetes",
        "ci/cd",
        "infrastructure as code"
    },

    "mlops": {
        "continuous integration",
        "continuous deployment",
        "model versioning",
        "data versioning",
        "experiment tracking",
        "pipeline automation",
        "model monitoring",
        "model retraining automation",
        "scalable model serving",
        "feature store management"
    },

    # ===== Software Engineering =====
    "software engineering": {
        "object oriented programming",
        "data structures",
        "algorithms",
        "design patterns",
        "testing",
        "code review"
    }
}

def build_reverse_ontology(ontology):
    reverse = {}
    for parent, children in ontology.items():
        for child in children:
            reverse.setdefault(child, set()).add(parent)
    return reverse
