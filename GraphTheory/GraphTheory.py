"""Graph theory p1"""

EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])};
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])};
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,4,5,6,7,3])};

def make_complete_graph(num_nodes):
    """make_complete_graph(num_nodes) -> dictionary"""
    temp = {};
    
    if num_nodes == 1:
        temp = {0: set([])};
    elif num_nodes > 1: 
        for item in range(0, num_nodes):
            edg = set();
            for jtem in range(num_nodes):
                if item != jtem:
                    edg.add(jtem); 
            
            temp[item] = edg;     
    return temp;

def compute_in_degrees(digraph):
    """compute_in_degrees(digraph) -> dictionary"""
    occurences = {};
    result = {};
    seen = set();
    for value in digraph.itervalues():
        for item in value:
            if item not in seen:
                result[item] = 1;
                seen.add(item);
            else:
                result[item] += 1;
    
    for key in digraph.iterkeys():
        if result.has_key(key):
            occurences[key] = result[key];
        else:
            occurences[key] = 0; 
    
    return occurences;    

def in_degree_distribution(digraph):
     """in_degree_distribution(digraph) -> dictionary"""
     in_degrees = compute_in_degrees(digraph);
     result = {};
     seen = set();
     for value in in_degrees.itervalues():
         if value != 0:
             if value not in seen:
                result[value] = 1;
                seen.add(value);
             else:
                result[value] += 1;
                seen.add(value);
     return result;       

#print make_complete_graph(2);
#print compute_in_degrees(EX_GRAPH1);
print in_degree_distribution(EX_GRAPH2);