import csv
from project import Project
import datetime


def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option")
    save_choice = input(f"Would you like to save to {filename}? (y/n): ").lower()
    if save_choice == 'y':
        save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a CSV file."""
    projects = []
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file, delimiter='\t')
        in_file.readline()  # Skip the header line
        for line in in_file:
            if line:  # Skip empty rows
                name, start_date, priority, estimate, completion = line
                projects.append(Project(name, start_date, priority, estimate, completion))
    return projects


def save_projects(filename, projects):
    """Save projects to a CSV file."""
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.estimate, project.completion])


def display_projects(projects):
    """Display all projects, separating incomplete and completed projects."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    """Filter projects that start after the given date."""
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.start_date > filter_date]
    print(f"Projects starting after {filter_date.strftime('%d/%m/%Y')}:")
    for project in sorted(filtered, key=lambda project: project.start_date):
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    new_project = Project(name, start_date, priority, estimate, completion)
    projects.append(new_project)


def update_project(projects):
    """Update a project based on the user's choice."""
    print("Select a project to update:")
    for i, project in enumerate(projects):
        print(f"{i}. {project}")
    try:
        project_index = int(input("Project choice: "))
        selected_project = projects[project_index]

        print(f"Selected project: {selected_project}")
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        selected_project.update(
            completion=int(new_completion) if new_completion else selected_project.completion,
            priority=int(new_priority) if new_priority else selected_project.priority
        )
    except (ValueError, IndexError):
        print("Invalid selection.")


if __name__ == "__main__":
    main()
