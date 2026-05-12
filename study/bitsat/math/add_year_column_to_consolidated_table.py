from bs4 import BeautifulSoup
import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def normalize_text(text):
    """
    Normalizes whitespace so that topic names still match even if the HTML
    table has line breaks, tabs, or multiple spaces inside a topic cell.
    """
    return " ".join(text.split())


def load_json_mapping(mapping_file):
    try:
        raw_mapping = json.loads(Path(mapping_file).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in mapping file: {mapping_file}\n{error}")

    return {
        normalize_text(topic): value
        for topic, value in raw_mapping.items()
    }


def find_target_table(soup, table_class):
    table = soup.find("table", class_=table_class)
    if table is None:
        raise ValueError(f'Could not find <table class="{table_class}">.')
    return table


def extract_topics_from_table(table):
    tbody = table.find("tbody")
    if tbody is None:
        raise ValueError("Could not find <tbody> in the table.")

    rows = tbody.find_all("tr")
    topics = []

    for index, row in enumerate(rows, start=1):
        cells = row.find_all("td")

        if len(cells) < 2:
            raise ValueError(f"Row {index} does not have Sl No and Topic columns.")

        topic = normalize_text(cells[1].get_text(" ", strip=True))
        topics.append(topic)

    return topics


def validate_mapping(year_mapping, topics):
    missing_topics = [topic for topic in topics if topic not in year_mapping]
    extra_topics = [topic for topic in year_mapping if topic not in topics]

    if missing_topics:
        raise ValueError(
            "The JSON mapping is missing these required topics:\n"
            + "\n".join(f"- {topic}" for topic in missing_topics)
        )

    if extra_topics:
        raise ValueError(
            "The JSON mapping contains extra/unexpected topics:\n"
            + "\n".join(f"- {topic}" for topic in extra_topics)
        )

    for topic in topics:
        if not isinstance(year_mapping[topic], list):
            raise ValueError(f'The value for "{topic}" must be a list of PYQ numbers.')

        for q in year_mapping[topic]:
            try:
                int(q)
            except ValueError:
                raise ValueError(
                    f'Invalid PYQ number "{q}" under topic "{topic}". '
                    "PYQ numbers must be integers."
                )


def make_pyq_links(year, pyq_numbers, subject_slug, base_folder):
    if not pyq_numbers:
        return "-"

    clean_numbers = sorted({int(q) for q in pyq_numbers})

    links = []

    for q in clean_numbers:
        href = (
            f"{base_folder}/"
            f"bitsat_{subject_slug}_pyqs_{year}/"
            f"bitsat_{subject_slug}_pyqs_{year}.html#Q{q}"
        )

        links.append(
            f'''<a
\thref="{href}"
\tclass="link_no_style"
\ttarget="_blank"
\t>{q}</a
><br />'''
        )

    return "\n".join(links)


def get_existing_years(header_row):
    headers = header_row.find_all("th")
    year_headers = headers[2:]

    years = []

    for th in year_headers:
        text = normalize_text(th.get_text(" ", strip=True))

        if not text.isdigit():
            raise ValueError(
                f'Expected year column after "Sl No" and "Topic", but found "{text}".'
            )

        years.append(int(text))

    return years


def get_insert_position(existing_years, new_year, sort_years_desc):
    if not sort_years_desc:
        return 2 + len(existing_years)

    all_years = sorted(existing_years + [new_year], reverse=True)
    return 2 + all_years.index(new_year)


def insert_tag_at_position(parent, new_tag, position):
    existing_element_children = [
        child for child in parent.children
        if getattr(child, "name", None) is not None
    ]

    if position >= len(existing_element_children):
        parent.append(new_tag)
    else:
        existing_element_children[position].insert_before(new_tag)


def add_year_column(
    existing_table_html,
    year_mapping,
    year,
    subject_slug,
    base_folder,
    table_class,
    sort_years_desc,
):
    soup = BeautifulSoup(existing_table_html, "html.parser")

    table = find_target_table(soup, table_class)

    thead = table.find("thead")
    tbody = table.find("tbody")

    if thead is None:
        raise ValueError("Could not find <thead> in the table.")

    if tbody is None:
        raise ValueError("Could not find <tbody> in the table.")

    header_row = thead.find("tr")
    if header_row is None:
        raise ValueError("Could not find header <tr> inside <thead>.")

    year = int(year)

    existing_headers = [
        normalize_text(th.get_text(" ", strip=True))
        for th in header_row.find_all("th")
    ]

    if len(existing_headers) < 2:
        raise ValueError("Table must have at least Sl No and Topic header columns.")

    if str(year) in existing_headers:
        raise ValueError(f"Year {year} already exists in the table.")

    topics = extract_topics_from_table(table)
    validate_mapping(year_mapping, topics)

    existing_years = get_existing_years(header_row)

    insert_position = get_insert_position(
        existing_years=existing_years,
        new_year=year,
        sort_years_desc=sort_years_desc,
    )

    new_th = soup.new_tag("th")
    new_th.string = str(year)
    insert_tag_at_position(header_row, new_th, insert_position)

    body_rows = tbody.find_all("tr")

    for index, row in enumerate(body_rows):
        topic = topics[index]
        pyq_numbers = year_mapping[topic]

        cell_html = make_pyq_links(
            year=year,
            pyq_numbers=pyq_numbers,
            subject_slug=subject_slug,
            base_folder=base_folder,
        )

        new_td = soup.new_tag("td")
        new_td.append(BeautifulSoup(cell_html, "html.parser"))

        insert_tag_at_position(row, new_td, insert_position)

    return soup.prettify(), topics


def get_unique_pyqs(year_mapping, topics):
    return sorted(
        {
            int(q)
            for topic in topics
            for q in year_mapping.get(topic, [])
        }
    )


def create_backup(file_path):
    source = Path(file_path)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = source.with_name(f"{source.stem}.backup_{timestamp}{source.suffix}")

    shutil.copy2(source, backup_path)

    return backup_path


def main():
    parser = argparse.ArgumentParser(
        description="Add a new year column to an existing consolidated HTML table."
    )

    parser.add_argument(
        "--table",
        required=True,
        help="Path to the existing consolidated HTML table file.",
    )

    parser.add_argument(
        "--mapping",
        required=True,
        help="Path to the JSON file containing topic-to-PYQ mapping for the new year.",
    )

    parser.add_argument(
        "--year",
        required=True,
        help="Year to add, for example 2024 or 2026.",
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Optional output file. Required unless --in-place is used.",
    )

    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Rewrite the input table file directly after creating a timestamped backup.",
    )

    parser.add_argument(
        "--sort-years-desc",
        action="store_true",
        help="Keep year columns in reverse chronological order after Sl No and Topic.",
    )

    parser.add_argument(
        "--subject-slug",
        required=True,
        help="Subject slug used in links, for example chem, phys, math.",
    )

    parser.add_argument(
        "--base-folder",
        required=True,
        help="Base folder path used in links, for example bitsat_chem_pyqs.",
    )

    parser.add_argument(
        "--table-class",
        default="blueprint-table",
        help="CSS class of the target table. Default: blueprint-table.",
    )

    args = parser.parse_args()

    if args.in_place and args.output:
        raise ValueError("Use either --in-place or --output, not both.")

    if not args.in_place and not args.output:
        raise ValueError("You must provide either --output or --in-place.")

    table_path = Path(args.table)

    if not table_path.exists():
        raise FileNotFoundError(f"Table file not found: {table_path}")

    year_mapping = load_json_mapping(args.mapping)
    existing_table_html = table_path.read_text(encoding="utf-8")

    updated_html, topics = add_year_column(
        existing_table_html=existing_table_html,
        year_mapping=year_mapping,
        year=args.year,
        subject_slug=args.subject_slug,
        base_folder=args.base_folder,
        table_class=args.table_class,
        sort_years_desc=args.sort_years_desc,
    )

    if args.in_place:
        backup_path = create_backup(table_path)
        table_path.write_text(updated_html, encoding="utf-8")
        output_path = table_path
    else:
        output_path = Path(args.output)
        output_path.write_text(updated_html, encoding="utf-8")
        backup_path = None

    unique_pyqs = get_unique_pyqs(year_mapping, topics)

    print(f"Added year column: {args.year}")

    if args.sort_years_desc:
        print("Year columns sorted in reverse chronological order.")

    if backup_path:
        print(f"Backup created: {backup_path}")

    print(f"Output file: {output_path}")

    print("Unique PYQs counted:")
    print(", ".join(str(q) for q in unique_pyqs))

    print(f"Total unique PYQ count: {len(unique_pyqs)}")


if __name__ == "__main__":
    main()