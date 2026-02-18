import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_insights(predictions_summary):
    """
    predictions_summary: dict with phase-wise key metrics
    Example:
    {
        "Learn": {"avg_health": 0.75, "top_drivers": ["engagement", "downloads"]},
        "Buy": {"avg_health": 0.62, "top_drivers": ["email_clicks", "trial_usage"]}
    }
    """
    prompt = f"Summarize the following customer health insights in business-friendly language:\n{predictions_summary}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=200
    )
    
    return response['choices'][0]['message']['content']