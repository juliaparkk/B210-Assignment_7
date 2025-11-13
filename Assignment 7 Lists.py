# Assignment 7 Lists.py
# Reads the CSV, groups songs by album into lists, sorts each list by duration_ms (descending),
# and writes a new CSV with rows grouped by album and sorted by duration.
# Uses only Python built-ins (no modules).

def split_csv_line(line):
    """Split a CSV line into fields, handling quotes and escaped double-quotes."""
    fields = []
    field = []
    i = 0
    in_quotes = False
    length = len(line)
    while i < length:
        c = line[i]
        if in_quotes:
            if c == '"':
                # Escaped quote -> add a single quote and skip the escape
                if i + 1 < length and line[i + 1] == '"':
                    field.append('"')
                    i += 2
                else:
                    in_quotes = False
                    i += 1
            else:
                field.append(c)
                i += 1
        else:
            if c == '"':
                in_quotes = True
                i += 1
            elif c == ',':
                fields.append(''.join(field))
                field = []
                i += 1
            else:
                field.append(c)
                i += 1
    fields.append(''.join(field))
    return fields

def csv_escape(value):
    """Escape a value for CSV output (simple): double internal quotes and quote if needed."""
    if value is None:
        value = ''
    s = str(value)
    if '"' in s:
        s = s.replace('"', '""')
    if ',' in s or '"' in s or '\n' in s:
        return '"' + s + '"'
    return s

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    if not lines:
        raise ValueError("Input file is empty")

    header = split_csv_line(lines[0])
    # locate columns
    try:
        duration_idx = header.index('duration_ms')
    except ValueError:
        raise ValueError("Header does not contain 'duration_ms' column")
    try:
        album_idx = header.index('album_name')
    except ValueError:
        raise ValueError("Header does not contain 'album_name' column")

    albums = {}  # album_name -> list of (duration_ms:int, row: list[str])

    for line in lines[1:]:
        if not line.strip():
            continue
        row = split_csv_line(line)
        # If row shorter than header, pad with empty strings
        if len(row) < len(header):
            row += [''] * (len(header) - len(row))
        album = row[album_idx]
        # parse duration
        dur_raw = row[duration_idx].strip()
        try:
            duration = int(dur_raw)
        except Exception:
            try:
                duration = int(float(dur_raw))
            except Exception:
                duration = 0
        albums.setdefault(album, []).append((duration, row))

    # sort each album's list by duration descending (largest first)
    for album_name in albums:
        albums[album_name].sort(key=lambda x: x[0], reverse=True)

    # write out grouped & sorted CSV
    # sort albums alphabetically for predictable output
    album_names = sorted(albums.keys(), key=lambda x: (x or '').lower())
    with open(output_path, 'w', encoding='utf-8', newline='\n') as out:
        out.write(','.join(csv_escape(h) for h in header) + '\n')
        for album_name in album_names:
            for duration, row in albums[album_name]:
                out.write(','.join(csv_escape(field) for field in row) + '\n')

    # return a lightweight mapping of album -> list of rows (without duration)
    return {a: [r for d, r in albums[a]] for a in album_names}

if __name__ == '__main__':
    input_path = r'c:\Users\jinas\Downloads\taylor_discography.csv'
    output_path = r'c:\Users\jinas\Downloads\taylor_by_album_sorted.csv'
    albums = process_file(input_path, output_path)
    total_rows = sum(len(rows) for rows in albums.values())
    print("Wrote:", output_path)
    print("Albums:", len(albums), "Total rows:", total_rows)