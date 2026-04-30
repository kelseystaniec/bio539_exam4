import sys

def validate_sequence(sequence, k):
  """Validates input sequence to determine if it's DNA
  
  Parameters:
    sequence(str): DNA sequence to be analyzed
    k(int): length of kmer
    
  Output:
    True/False for whether or not sequence meets the requirements
  """
  if len(sequence) < k or k < 1: #stop if the sequence is shorter thean the kmer size or if the size is either 0 or negative
    return False
  for nucleotide in sequence:
    if nucleotide in '1234567890': #stop if there is a number
      return False
    if nucleotide not in{'A', 'C', 'T', 'G'}: #stop if there is a letter that's not A,C,T,G
      return False
  return True
          
def update_kmer_count(kmer_data, kmer, next_char):
  """Creates dictionary for kmer data including number of occurences and next characters
  
  Parameters:
    kmer_data(dict): dictionary for kmer data. Starts as empty
    kmer(str): kmer of length k sliced from sequence
    next_char(str): character in sequence directly after kmer
  
  Output:
    kmer_data(dict): updated dictionary with all kmers, counts, and next characters with their counts
  """
  
  if kmer not in kmer_data: #check if the kmer is already in the dictionary
    kmer_data[kmer] = {'count': 0, 'next_chars': {}} #add kmer to the dictionary 
  kmer_data[kmer]['count'] += 1 #add 1 to the kmer count
    
  if next_char !='':
    if next_char not in kmer_data[kmer]['next_chars']: #check if next_char is already in the dictionary for that particular kmer
      kmer_data[kmer]['next_chars'][next_char] = 0 #create a spot for the next_char and fill with 0
    kmer_data[kmer]['next_chars'][next_char] += 1 #add 1 to the next_char count
      
  return kmer_data

def count_kmers_with_context(sequence, k):
  """Count kmers and next characters without them being explicitly given: find them in sequence
  
  Parameters:
    sequence(str): validated DNA sequence
    k(int): length of kmer
    
  Output:
    kmer_data(dict): updated dictionary with all kmers, counts, and next characters with their counts
  """
  kmer_data = {} #initialize dictionary
    
  for i in range(len(sequence) - (k-1)): #loop through every letter until you're k-1 from end of sequence. This ensures you get the last kmer
    kmer = sequence[i:i+k] #kmer is defined as sequence from i to i+k (noninclusive)
    if (i+k) < len(sequence): #make sure kmer doesn't go to end of sequence
      next_char = sequence[i+k] #get next character
    else:
      next_char = '' #if kmer does go to end of sequence, next_char is blank
        
    kmer_data = update_kmer_count(kmer_data, kmer, next_char) #add to dictionary
    
  return kmer_data


def write_results_to_file(kmer_data, output_filename):
  """Takes kmer_data dictionary and puts it in an accessible output file
  
  Parameters:
    kmer_data(dict): dictionary generated from count_kmers_with_context
    output_filename(txt): text file that the results will be written into
    
  Output:
    output_filename(txt):text file with results written in
  """
  sorted_kmers = sorted(kmer_data.keys()) #sorts kmers in alaphabetical order
    
  with open(output_filename, 'a') as f: #opens outputfile and will append to whatever is already in there
    for kmer in sorted_kmers: #loop through kmer list
      next_chars = kmer_data[kmer]['next_chars'] #Get the next characters for each kmer
            
      #Create a string of the next characters instead of them being separate list items
      next_char_str = " ".join(
        f"{char}:{freq}" 
        for char, freq in sorted(next_chars.items()) #sort alphabetically
      )
            
      f.write(f"{kmer} {next_char_str}\n") #in output file, write each kmer followed by its string of next characters and counts


def main():
  """Takes a file of DNA sequences and outputs a file of all kmers and next characters
  
  Parameters: 1,2,3 on command line
    sequence_file(txt): raw input file with DNA sequences
    k(int): length of kmer
    output_file(txt): empty file to write into
    
  Output:
    output_file(txt): text file with results written in
  """
  sequence_file = sys.argv[1] #input file is first thing on command line
  k = int(sys.argv[2]) #k number is second thing on command line
  output_file = sys.argv[3] #output file name is third thing on command line
    
  print(f"Reading sequences from {sequence_file}...") #print to know process has started

  with open(sequence_file, 'r') as f: #open input file
    for sequence in f:
      sequence = sequence.strip() #removes everything from each sequence except the string

      if not validate_sequence(sequence, k): #runs through validate_sequence function and skips if it doesn't meet the criteria
        print(f"  Warning: Skipping sequence")
        continue 
            
      kmer_data = count_kmers_with_context(sequence, k)  #creates kmer_data dictionary
            
      write_results_to_file(kmer_data, output_file) #writes dictionary to output file

#Run the script
if __name__ == '__main__':
  main()
