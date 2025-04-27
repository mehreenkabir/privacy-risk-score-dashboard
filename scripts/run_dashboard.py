import os
from data_scanner import scan_dataset
from dashboard_generator import generate_html_dashboard

def main():
    data_dir = "data"
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    scores = {}

    for file in files:
        dept_name = file.replace('_data.csv', '').capitalize()
        file_path = os.path.join(data_dir, file)
        score = scan_dataset(file_path)
        scores[dept_name] = score

    generate_html_dashboard(scores)

if __name__ == "__main__":
    main()

