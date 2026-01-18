SKILL_ONTOLOGY = {

    # ===== Core AI / ML =====
    "artificial intelligence": {
        "machine learning",
        "knowledge representation",
        "expert systems",
        "search algorithms"
    },

    "machine learning": {
        "supervised learning",
        "unsupervised learning",
        "reinforcement learning",
        "deep learning",
        "nlp",
        "computer vision"
    },

    "deep learning": {
        "neural networks",
        "cnn",
        "rnn",
        "lstm",
        "transformers"
    },

    "nlp": {
        "tokenization",
        "text classification",
        "named entity recognition",
        "sentiment analysis"
    },

    "computer vision": {
        "image classification",
        "object detection",
        "image segmentation"
    },

    # ===== Programming =====
    "programming": {
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript"
    },

    "python": {
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn"
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
        "data visualization"
    },

    "data science": {
        "data analysis",
        "machine learning",
        "statistics"
    },

    # ===== Databases =====
    "databases": {
        "sql",
        "mysql",
        "postgresql",
        "mongodb"
    },

    # ===== Cloud / DevOps =====
    "cloud": {
        "aws",
        "azure",
        "gcp"
    },

    "devops": {
        "docker",
        "kubernetes",
        "ci/cd"
    },

    # ===== Software Engineering =====
    "software engineering": {
        "object oriented programming",
        "data structures",
        "algorithms",
        "design patterns"
    }
}

def build_reverse_ontology(ontology):
    reverse = {}
    for parent, children in ontology.items():
        for child in children:
            reverse.setdefault(child, set()).add(parent)
    return reverse
