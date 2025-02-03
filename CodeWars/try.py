# def greet():
#     return f"hello world!"



# DNA
# def DNA_strand(dna):
#     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     return ''.join(complement[base] for base in dna)



# import math
# from typing import Union

# def calculate_tip(amount: Union[float, int], rating: str) -> Union[int, str]:
#     ratings = {
#         "terrible": 0,
#         "poor": 0.05,
#         "good": 0.1,
#         "great": 0.15,
#         "excellent": 0.2
#     }
    
#     standard_rating = rating.lower()
    
#     if standard_rating in ratings:
#         tip = math.ceil(amount * ratings[standard_rating])  # Always round up
#         return tip
#     else:
#         return "Rating not recognised"



# import math
# def grow(arr):
#     return math.prod(arr)
