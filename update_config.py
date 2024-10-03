import json
import os

# Function to load configuration from a JSON file
def load_config(file_path):
    if not os.path.exists(file_path):
        print(f"Configuration file {file_path} not found.")
        return None
    
    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
            return config
        except json.JSONDecodeError:
            print("Error decoding JSON from the configuration file.")
            return None

# Function to save the updated configuration to a JSON file
def save_config(file_path, config):
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
        print("Configuration updated successfully.")
    except Exception as e:
        print(f"An error occurred while saving the configuration: {e}")

# Function to validate the configuration structure
def validate_config(config):
    required_keys = ["name", "age", "company", "experience", "courses"]
    for key in required_keys:
        if key not in config:
            print(f"Missing required key: {key}")
            return False
    
    if not isinstance(config["courses"], list):
        print("Courses should be a list.")
        return False
    
    return True

# Main function to run the application
def main():
    config_file = 'config.json'
    config = load_config(config_file)
    
    if config is None or not validate_config(config):
        return

    print("Current Configuration:")
    print(json.dumps(config, indent=4))
    
    # User input for updating information
    name = input("Enter name (current: {}): ".format(config['name'])) or config['name']
    age = input("Enter age (current: {}): ".format(config['age']))
    company = input("Enter company (current: {}): ".format(config['company'])) or config['company']
    experience = input("Enter years of experience (current: {}): ".format(config['experience']))
    courses = input("Enter courses (comma-separated, current: {}): ".format(", ".join(config['courses']))) or ", ".join(config['courses'])

    # Update the configuration
    config['name'] = name
    config['age'] = int(age) if age.isdigit() else config['age']
    config['company'] = company
    config['experience'] = int(experience) if experience.isdigit() else config['experience']
    config['courses'] = [course.strip() for course in courses.split(",")]

    # Validate and save the updated configuration
    if validate_config(config):
        save_config(config_file, config)

if __name__ == "__main__":
    main()
