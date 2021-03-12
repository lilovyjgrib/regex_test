import re


def find_refs(file):
    reg_for_references_block = "\nReferences\n.+?\n\d+?\n"
    raw_refs = re.findall(reg_for_references_block, file, flags=re.DOTALL)
    refs_list = []
    reg_for_single_refs = r'\n\[\d+?\] (.*?)(?:\[|\n\n)'
    for ref in raw_refs:
        refs_list.extend(re.findall(reg_for_single_refs, ref, flags=re.DOTALL))
    return refs_list


def split_authors(line):
    authors = re.search(r'^[A-Z].+?\.[ \n]', line, flags=re.MULTILINE)
    if authors:
        authors = authors[0].strip()
        publication = line.split(authors)[1].strip()
    else:
        publication = line.strip()
        authors = ''
    return authors, publication


with open('proceedings.txt', 'r', encoding='utf_8') as f:
    f_line = f.read()
    all_refs = find_refs(f_line)
    for i in all_refs:
        print(i)
    refs_split = [split_authors(i) for i in all_refs]
    for i in refs_split:
        print(i)
