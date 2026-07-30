# Secure Student Academic Portal — Lab: Encapsulation & Secure Class Design

Course: Introduction to Advanced Level Programming  
Activity: Independent Lab — Encapsulation & Secure Class Design  
Due: 29 July 2026, 11:30 PM

Overview
--------
Implement a Secure Student module that enforces encapsulation: sensitive student state (CGPA, tuition balance, etc.) must not be modified directly and must be changed only via validated methods.

Deliverables
----------
- student_uml.png — UML class diagram (render from student_uml.puml)
- secure_student.py — implementation of the Student class with validated accessors/mutators
- test_secure_student.py — pytest unit tests
- README.md — (this file) with instructions

How to render the UML PNG
-------------------------
Option A (local PlantUML + Graphviz):
1. Install Graphviz.
2. Install PlantUML (jar).
3. Run: java -jar plantuml.jar student_uml.puml
This produces student_uml.png in the same folder.

Option B (online PlantUML server):
1. Paste the contents of student_uml.puml into https://www.plantuml.com/plantuml/ and generate the PNG.

How to run tests
---------------
1. Create a virtualenv and install pytest:
   python -m venv .venv
   source .venv/bin/activate   # or .venv\\Scripts\\activate on Windows
   pip install pytest
2. Run:
   pytest -q

Suggested repo name and branch
------------------------------
vnsgodwill-collab/secure-student-portal (branch: main)

Create & push (commands)
------------------------
If you want to create and push locally, run these commands (replace values where needed):

# Create local repo and commit
mkdir secure-student-portal && cd secure-student-portal
# Put the files student_uml.puml, secure_student.py, test_secure_student.py, README.md in this folder
git init
git add .
git commit -m "Initial commit: secure student module, tests, UML"

# Create repository on GitHub using gh CLI (or create via web)
gh repo create vnsgodwill-collab/secure-student-portal --public --source=. --remote=origin --push

# OR, if you prefer to create the repo on the website, create it and then:
git branch -M main
git remote add origin https://github.com/vnsgodwill-collab/secure-student-portal.git
git push -u origin main

Inviting instructor (you said you'll add them yourself)
-------------------------------------------------------
Once the repo exists, add collaborators:
- On GitHub: Settings → Manage access → Invite a collaborator → enter instructor username
- Or with gh CLI:
  gh api -X PUT /repos/vnsgodwill-collab/secure-student-portal/collaborators/INSTRUCTOR_USERNAME -f permission="push"

Notes
-----
- The Python implementation demonstrates encapsulation by providing read-only accessors and validated mutators. Python's naming convention (underscore) is used to indicate privacy; unit tests exercise the public API.
- If you want a stricter language (e.g., Java or C#) with enforced private fields, tell me and I’ll produce that variant.

Next steps
----------
1) If you want me to push the prepared files, create the empty repo vnsgodwill-collab/secure-student-portal and grant me push access (or invite me as a collaborator), then reply here with "Repo created" and I will push the files.  
2) Or run the commands above yourself to create the repo and push.  
3) If you’d like, I can also add a GitHub Actions workflow to run pytest automatically — say “add CI” and I’ll include it.

Which of these do you want me to do next?