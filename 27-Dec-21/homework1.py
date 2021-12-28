"""
The exponential explosion in origami. 
Zhang San has a very large piece of paper with a thickness of about 0.08mm. 
In theory, how many times can it be folded in half to reach the height of Mount Everest (8848.13 meters).
"""

folds = 0 
paper_thickness = 0.00008 # paper thickness in metres

while paper_thickness < 8848.13: # as long as the paper is thinner than 8843.13 metres
    paper_thickness *= 2 # double the paper thickness (fold the paper)
    folds += 1 

print(folds)