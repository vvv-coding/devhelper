#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


STEP_PATTERN = re.compile(r"^##\s*Step\s+(\d+)\s*[:\-]?\s*(.*)$", re.IGNORECASE)


def parse_steps(markdown_text: str) -> dict[int, str]:
	lines = markdown_text.splitlines()
	steps: dict[int, str] = {}
	current_step = None
	buffer: list[str] = []

	for line in lines:
		match = STEP_PATTERN.match(line.strip())
		if match:
			if current_step is not None:
				steps[current_step] = "\n".join(buffer).strip()

			current_step = int(match.group(1))
			buffer = [line]
			continue

		if current_step is not None:
			buffer.append(line)

	if current_step is not None:
		steps[current_step] = "\n".join(buffer).strip()

	return steps


def get_lab_file(lab_number: int) -> Path:
	possible_dirs = [
		Path(__file__).resolve().parent / "lab",  
		Path("/app/lab"), 
		Path.cwd() / "lab", 
	]
	
	for base_lab_dir in possible_dirs:
		lab_path = base_lab_dir / f"Lab{lab_number}.md"
		if lab_path.exists():
			return lab_path
	
	return possible_dirs[0] / f"Lab{lab_number}.md"


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Print a specific step from a lab markdown file, or the full lab.",
	)
	parser.add_argument("--lab", type=int, required=True, help="Lab number, for example: 1")
	parser.add_argument(
		"--step",
		type=int,
		help="Step number, for example: 2. If omitted, prints the full lab.",
	)
	args = parser.parse_args()

	lab_path = get_lab_file(args.lab)
	if not lab_path.exists():
		raise SystemExit(f"Lab file not found: {lab_path}")

	markdown_text = lab_path.read_text(encoding="utf-8")
	if args.step is None or args.step == 0:
		print(markdown_text)
		return

	steps = parse_steps(markdown_text)

	if args.step not in steps:
		available = ", ".join(str(number) for number in sorted(steps.keys())) or "none"
		raise SystemExit(
			f"Step {args.step} not found in lab {args.lab}. Available steps: {available}"
		)

	print(steps[args.step])


if __name__ == "__main__":
	main()