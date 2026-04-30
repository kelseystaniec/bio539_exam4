#!/usr/bin/env python3
import pytest

from kmer_analyzer import validate_sequence

#Validates whether the sequence is actually a DNA string
def test_validate_sequence_basic():
  sequence = "GCCTGA"
  k = 2
  result = validate_sequence(sequence, k)
  exp = True
  assert result==exp

#Deal with numbers  
def test_validate_sequence_number():
  sequence = "GC4TGA"
  k = 2
  result = validate_sequence(sequence, k)
  exp = False
  assert result==exp

#Deal with other letters/characters
def test_validate_sequence_nondna():
  sequence = "GCBTGA"
  k = 2
  result = validate_sequence(sequence, k)
  exp = False
  assert result==exp

#Deal with empty space
def test_validate_sequence_empty():
  sequence = ""
  k = 2
  result = validate_sequence(sequence, k)
  exp = False
  assert result==exp

#Deal with negative kmer size
def test_validate_sequence_negsize():
  sequence = "GCCTGA"
  k = -2
  result = validate_sequence(sequence, k)
  exp = False
  assert result==exp


from kmer_analyzer import update_kmer_count

#Basic test
def test_update_kmer_count_basic():
  kmer_data = {}
  kmer = "GCCT"
  next_char = "G"
  result = update_kmer_count(kmer_data, kmer, next_char)
  exp =  {"GCCT": {"count": 1, "next_chars": {"G": 1}}}
  assert result==exp

#Deal with kmer at end of line
def test_update_kmer_count_end():
  kmer_data = {}
  kmer = "GCCT"
  next_char = ""
  result = update_kmer_count(kmer_data, kmer, next_char)
  exp =  {"GCCT": {"count": 1, "next_chars": {}}}
  assert result==exp

#Make sure duplicates get added  
def test_update_kmer_count_duplicate():
  kmer_data = {"GCCT": {"count": 1, "next_chars": {}}}
  kmer = "GCCT"
  next_char = "G"
  result = update_kmer_count(kmer_data, kmer, next_char)
  exp =  {"GCCT": {"count": 2, "next_chars": {"G": 1}}}
  assert result==exp

#Make sure several new characters can get added to same kmer
def test_update_kmer_count_newchar():
  kmer_data = {"GCCT": {"count": 1, "next_chars": {"G": 1}}}
  kmer = "GCCT"
  next_char = "A"
  result = update_kmer_count(kmer_data, kmer, next_char)
  exp =  {"GCCT": {"count": 2, "next_chars": {"G": 1,"A": 1}}}
  assert result==exp


from kmer_analyzer import count_kmers_with_context

#Basic test
def test_count_kmers_with_context_basic():
  kmer_data = {}
  sequence = "ATAT"
  k = 2
  result = count_kmers_with_context(sequence, k)
  exp = {"AT": {"count": 2, "next_chars": {"A": 1}},"TA":{"count": 1, "next_chars": {"T": 1}}}
  assert result==exp

#Deal with k larger than sequence
def test_count_kmers_with_context_bigk():
  kmer_data = {}
  sequence = "ATAT"
  k = 5
  result = count_kmers_with_context(sequence, k)
  exp = {}
  assert result==exp

#Deal with k equal to sequence
def test_count_kmers_with_context_equalk():
  kmer_data = {}
  sequence = "ATAT"
  k = 4
  result = count_kmers_with_context(sequence, k)
  exp = {"ATAT": {"count": 1, "next_chars": {}}}
  assert result==exp


from kmer_analyzer import write_results_to_file

#Basic test
def test_write_results_to_file_basic(tmp_path):
  kmer_data = {"GCCT": {"count": 1, "next_chars": {"G": 1}},"GCAT": {"count": 2, "next_chars": {"G": 1,"C":1}}}
  output_file = tmp_path/"test_kmer_data.txt"
  result = write_results_to_file(kmer_data, output_file)
  content = output_file.read_text()
  exp = "GCAT C:1 G:1\nGCCT G:1\n"
  assert content == exp

#Empty dictionary
def test_write_results_to_file_empty(tmp_path):
  kmer_data = {}
  output_file = tmp_path/"test_kmer_data.txt"
  result = write_results_to_file(kmer_data, output_file)
  content = output_file.read_text()
  exp = ""
  assert content == exp





