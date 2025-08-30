import sys
import os
import json
from collections import Counter

class LogAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.logs = []

    def parse_log(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(f"Log file not found: {self.filepath}")
        if self.filepath.endswith('.json'):
            self._parse_json_log()
        elif self.filepath.endswith('.txt'):
            self._parse_txt_log()
        else:
            raise ValueError("Unsupported log file format. Please use .txt or .json")

    def _parse_json_log(self):
        with open(self.filepath, 'r') as file:
            self.logs = json.load(file)

    def _parse_txt_log(self):
        with open(self.filepath, 'r') as file:
            self.logs = file.readlines()

    def summarize_logs(self):
        summary = Counter()
        for log_entry in self.logs:
            summary[self._classify_log(log_entry)] += 1
        return summary

    def _classify_log(self, log_entry):
        if 'ERROR' in log_entry:
            return 'ERROR'
        elif 'WARNING' in log_entry:
            return 'WARNING'
        else:
            return 'INFO'

def main(filepath):
    analyzer = LogAnalyzer(filepath)
    analyzer.parse_log()
    summary = analyzer.summarize_logs()
    print("Log Summary:")
    for log_type, count in summary.items():
        print(f"{log_type}: {count}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py path/to/logfile.log")
    else:
        main(sys.argv[1])
