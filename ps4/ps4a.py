# Problem Set 4A
# Name: Jeremiah Flaga
# Collaborators:
# Time Spent: x:xx
# Started coding:  July 28, 2017 11:46 PM
# Finished coding: July 29, 2017 12:15 AM

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    

    if len(sequence) <= 1:
        #print([sequence])
        return [sequence]
    else:
        permutations = []
        first_char = sequence[0]
        next_chars = sequence[1:]
        permutations_of_subsequence = get_permutations(next_chars)
        for seq in permutations_of_subsequence:
            for index in range(len(seq) + 1):
                new_seq = seq[0:index] + first_char + seq[index:len(seq)+1]
                permutations.append(new_seq)
           
        #print(permutations)
        return permutations
   
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations('ab'))
    print(get_permutations('abc'))
    print(get_permutations('bust'))

