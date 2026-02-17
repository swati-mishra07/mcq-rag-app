import evaluate

# Load metrics once (efficient)
rouge = evaluate.load("rouge")
bleu = evaluate.load("bleu")
bertscore = evaluate.load("bertscore")


def evaluate_generation(prediction, reference):

    # -----------------------
    # ROUGE
    # -----------------------
    rouge_score = rouge.compute(
        predictions=[prediction],
        references=[reference]
    )

    # -----------------------
    # BLEU
    # -----------------------
    bleu_score = bleu.compute(
        predictions=[prediction],
        references=[[reference]]
    )

    # -----------------------
    # BERTScore
    # -----------------------
    bert_score = bertscore.compute(
        predictions=[prediction],
        references=[reference],
        lang="en"
    )

    return {
        "ROUGE-L": round(rouge_score["rougeL"], 4),
        "BLEU": round(bleu_score["bleu"], 4),
        "BERTScore-F1": round(bert_score["f1"][0], 4)
    }
