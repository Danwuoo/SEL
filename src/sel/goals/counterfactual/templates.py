"""Simple prompt templates for counterfactual tasks."""

TEMPLATES = {
    "robustness": "Rewrite the following task to test robustness:\n{prompt}",
    "error_correction": "This task previously failed. Revise it: {prompt}",
}
