from transformers import pipeline

analyze = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

feedbacks = [
    "The product is amazing! I love it!",
    "Terrible service, I am very disappointed.",
    "This is a great experience, I will buy again.",
    "Worst purchase I’ve ever made. Completely dissatisfied.",
    "I'm happy with the quality, but the delivery was delayed."
]

for fb in feedbacks:
    result = analyze(fb)[0]
    print(f"Feedback: {fb}\nSentiment: {result['label']} (Confidence: {result['score']:.2f})\n")
