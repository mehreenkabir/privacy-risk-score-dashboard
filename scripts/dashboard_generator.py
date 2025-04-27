import os

def generate_html_dashboard(scores, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "privacy_risk_dashboard.html")

    html_content = """
    <html>
    <head><title>Privacy Risk Dashboard</title></head>
    <body>
        <h1>Privacy Risk Scores by Department</h1>
        <table border="1" cellpadding="8" cellspacing="0">
            <tr>
                <th>Department</th>
                <th>Risk Score</th>
                <th>Risk Level</th>
            </tr>
    """

    for dept, score in scores.items():
        if score >= 30:
            level = "High"
        elif score >= 15:
            level = "Moderate"
        else:
            level = "Low"
        html_content += f"""
            <tr>
                <td>{dept}</td>
                <td>{score}</td>
                <td>{level}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(report_path, "w") as f:
        f.write(html_content)

    print(f"Dashboard saved to: {report_path}")

