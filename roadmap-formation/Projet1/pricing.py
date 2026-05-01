
PRICING = {
    "gpt-4o":         {"input": 2.50,  "output": 10.00, "context": 128_000},
    "gpt-4o-mini":    {"input": 0.15,  "output": 0.60,  "context": 128_000},
    "claude-sonnet":  {"input": 3.00,  "output": 15.00, "context": 200_000},
    "claude-haiku":   {"input": 0.80,  "output": 4.00,  "context": 200_000},
    "local":          {"input": 0.00,  "output": 0.00,  "context": 8_000},
}



def estimate_cost(input_tokens, output_tokens, model):

    prix = PRICING[model]

    cout_input = input_tokens * (prix["input"] / 1_000_000)
    cout_ouput = output_tokens * (prix["output"] / 1_000_000)

    total = cout_input + cout_ouput

    return    {
        "input": cout_input,
        'output': cout_ouput,
        "total":total
    }
