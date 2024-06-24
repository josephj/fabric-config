import subprocess
import inquirer

# Function to fetch the list of available models
def list_models():
    result = subprocess.run(['fabric', '--listmodels'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    # Filter out lines that are headers or empty
    models = [line for line in lines if line and not line.endswith(':')]
    return models

# Function to fetch the list of available patterns
def list_patterns():
    result = subprocess.run(['fabric', '--list'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    # Filter out lines that are headers or empty
    patterns = [line for line in lines if line and not line.endswith(':')]
    return patterns

def main():
    models = list_models()
    patterns = list_patterns()

    questions = [
        inquirer.List('model',
                      message="Select a model",
                      choices=models,
                      default="gpt-4o"),
        inquirer.List('pattern',
                      message="Select a pattern",
                      choices=patterns,
                      default="ai"),
    ]

    answers = inquirer.prompt(questions)

    print(f"You selected model: {answers['model']}")
    print(f"You selected pattern: {answers['pattern']}")

if __name__ == "__main__":
    main()
