readme file for Exam 4
Kelsey Staniec
April 22 2026

This script is intended to be the first steps in genome assembly. It will take an input file of sequences and output a file listing each kmer of a given length, how many times it appears, the character after it, and how many times each of those appears.

To run on command line:
  python kmer_analyzer.py <input_sequence_file> <k> <output_file>
  
k should be an integer equal to the length of each kmer

Test input file: test_sequences
Test output: test_kmer_data

Test conditions can be run using pytest and the test_scripts.py file

AI Usage:
-Ideas for test conditions
-Merging of the dictionaries for each separate sequence
-Explanation for some of the given code that I was unfamiliar with
-Miscellaneous bug fixes (typos, wrong data types, etc.)