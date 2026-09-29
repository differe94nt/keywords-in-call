#!/usr/bin/env python3
"""Inspect a locally downloaded PELIC_compiled.csv; no network requests.

python3 extract_pelic.py PELIC_compiled.csv --list
python3 extract_pelic.py PELIC_compiled.csv --learner YOUR_ID --output learner.csv

Defaults to writing classes (class_id=w). Retains original text; omits token/POS
columns to make the personal analysis copy manageable. Follow the source licence
before sharing any extracts. Task prompts remain in the official question.csv.
"""
import argparse
import collections
import csv
import pathlib
import sys

FIELDS = ['answer_id', 'anon_id', 'L1', 'semester', 'placement_test',
          'course_id', 'level_id', 'class_id', 'question_id', 'version',
          'text_len', 'text']


def rows(path, all_classes):
    csv.field_size_limit(10_000_000)
    with path.open(encoding='utf-8-sig', newline='') as source:
        reader = csv.DictReader(source)
        missing = set(FIELDS) - set(reader.fieldnames or [])
        if missing:
            raise ValueError('Not the expected compiled CSV. Missing columns: '
                             + ', '.join(sorted(missing))
                             + '. Check that you downloaded data, not a Git LFS pointer.')
        for row in reader:
            if None in row or any(row[k] is None for k in FIELDS):
                raise ValueError('Incomplete CSV row; download the complete file first.')
            if all_classes or row['class_id'] == 'w':
                yield row


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('csv_file', type=pathlib.Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--list', action='store_true', help='List 20 IDs with most unique text IDs')
    mode.add_argument('--learner', help='Exact anonymous learner ID')
    parser.add_argument('--all-classes', action='store_true')
    parser.add_argument('--output', type=pathlib.Path, default=pathlib.Path('learner.csv'))
    args = parser.parse_args()
    try:
        if args.list:
            counts = collections.defaultdict(set)
            for row in rows(args.csv_file, args.all_classes):
                counts[row['anon_id']].add(row['answer_id'])
            print('anon_id\tunique_text_ids')
            for learner, ids in sorted(counts.items(), key=lambda x: (-len(x[1]), x[0]))[:20]:
                print(f'{learner}\t{len(ids)}')
            print('Inspect task and version fields: different text IDs can still be related drafts.')
        else:
            selected = [r for r in rows(args.csv_file, args.all_classes)
                        if r['anon_id'] == args.learner]
            if not selected:
                raise ValueError('No matching records. Check --list and the class filter.')
            # Exclusive creation prevents overwriting the source or an existing analysis.
            with args.output.open('x', encoding='utf-8', newline='') as output:
                writer = csv.DictWriter(output, fieldnames=FIELDS, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(selected)
            print(f'Wrote {len(selected)} records to {args.output}. Inspect tasks and versions before selecting samples.')
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
