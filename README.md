# 🎮 Number Cruncher: Rebooted

**Number Cruncher: Rebooted** is a modern, curriculum-aligned educational math game for students in **Preschool through 5th Grade**, inspired by the classic *Number Munchers*. Built with Godot and Docker, it supports local play, classroom deployments, adaptive learning, and performance analytics for teachers.

---

## 📚 Features

| Category              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| 🎓 Grade Levels       | Preschool to 5th grade, aligned with core math standards                    |
| 🧮 Math Modes         | Counting, shapes, multiplication, division, fractions, algebra, and more     |
| 🧠 Adaptive Learning  | Difficulty scales dynamically based on student performance                  |
| 📊 Progress Reports   | Tracks accuracy, speed, completion rate, and topic proficiency               |
| 📝 Mini-Quizzes       | Short recap quizzes after each level to reinforce learning                   |
| 🎉 Rewards & Minigames| Unlockable games for mastering skills                                       |
| 👨‍🏫 Teacher Dashboard | Separate container for managing multiple students in a classroom             |
| 🐳 Docker Deployment  | Run anywhere: Windows, Linux, macOS, or browser — fully containerized        |
| 🖥️ Native Builds      | Exported Godot builds for standalone offline use                             |

---

## 🏗️ Project Structure
NumberCruncher-Rebooted/
├── game/ # Godot game files
├── docker/ # Dockerfiles for student/admin containers
├── admin-dashboard/ # Flask or FastAPI web dashboard for teachers
├── curriculum/ # JSON data for level configs and question pools
├── docs/ # Roadmaps, design docs, UI mockups
└── README.md


---

## 🚀 Getting Started

### Option 1: Run in Docker (Recommended for classrooms)
```bash
# Create a network for communication
docker network create cruncher_net

# Start the admin dashboard
docker run -d --name cruncher-admin \
  --network cruncher_net \
  -p 5000:5000 \
  ghcr.io/your-org/numbercruncher-admin

# Start a student container (repeat for each student)
docker run -d --name cruncher-student \
  --network cruncher_net \
  -e REPORT_URL=http://cruncher-admin:5000/report \
  ghcr.io/your-org/numbercruncher-student





Option 2: Run the Game Natively
Download the precompiled version for your platform from the Releases tab.

🔐 Teacher/Admin Dashboard
The teacher dashboard receives performance data from all connected student instances and displays:

Student names and grade levels

Mastery by topic

Time spent per session

Accuracy and trends over time

Exportable reports (CSV/JSON)

🧠 Curriculum Coverage
Grade	Topics Included
Preschool	Number recognition, counting, basic shapes
1st Grade	Addition, subtraction, comparing numbers, skip counting
2nd Grade	Even/odd, place value, simple fractions
3rd Grade	Multiplication, division, geometry, measurement
4th Grade	Factors/multiples, decimals, equivalent fractions
5th Grade	Algebraic expressions, coordinate grid, PEMDAS, volume


🧩 Want to Contribute?
We welcome contributions! Start with:

Checking issues

Reviewing the roadmap

Submitting pull requests with new levels, fixes, or improvements


🙌 Special Thanks
Inspired by the classic Number Munchers — reimagined for a new generation of learners.
Built with ❤️ using Godot Engine and Docker


📜 License
Number Cruncher: Rebooted is licensed under the GNU General Public License v3.0.

This means:

You can freely use, modify, and redistribute the code

If you distribute your own version, it must remain under GPL v3

It’s built to stay free and open for everyone, forever

See the full license here.
