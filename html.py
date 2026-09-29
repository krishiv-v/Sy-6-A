import re

webpage = """
<html>
<head>
    <title>Student Portfolio</title>
</head>
<body>
    <h1>My Portfolio</h1>
    <p>Welcome to my webpage.</p>
    <div>About Me</div>
    <table>
        <tr>
            <td>Subject</td>
            <td>Marks</td>
        </tr>
    </table>
</body>
</html>
"""

# Regex pattern to find selected opening HTML tags
tag_pattern = r"<(h1|p|div|table)\b[^>]*>"

found_tags = re.findall(tag_pattern, webpage, re.IGNORECASE)

print("Selected HTML Tags:")
print("-------------------")

for item in found_tags:
    print(f"<{item}>")

print("\nNumber of tags found:", len(found_tags))