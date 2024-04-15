import numpy as np

########################################################################################################################

def create_bingo_cards(number, rows=5, cols=5, pool=75, free_cells=0, fc_type=None):

    result = {}

    for n in range(1, number + 1):
    
        card = np.zeros((rows, cols), dtype=int)

        for i in range(cols):
            
            #start range and end range for each column based on the rules of bingo from wikipedia, this is subject to pool and cols to be expanded upon to unconventional bingo cards
            start_range = (i * (pool // cols)) + 1
            end_range = ((i + 1) * (pool // cols)) + 1
            
            start_range = int(start_range)
            end_range = int(end_range)
            
            column_numbers = np.random.choice(np.arange(start_range, end_range), size=rows, replace=False) 
            
            card[:,i] = column_numbers
        
        #free cells locationing logic
        if free_cells > 0:
            random_cells = None
            
            #ensure center is at least filled
            center = (rows // 2, cols // 2)
            card[center[0]][center[1]] = 0

            if free_cells > 1:
                
                if fc_type == "Random": #randomly assigns free cells 
                    possible_indices = list(set(range(rows * cols)) - {center[0] * cols + center[1]}) #ensures free cell is not selected again
                    random_cells = np.random.choice(possible_indices, free_cells - 1, replace=False)

                elif fc_type == "Diamond": #assigns free cells using manhattan distance
                    
                    distances = np.zeros((rows, cols))
                    for i in range(rows):
                        for j in range(cols):
                            distances[i, j] = abs(i - center[0]) + abs(j - center[1])

                    random_cells = np.argsort(distances.flatten())[:free_cells]

            if random_cells is not None:
                for idx in random_cells:
                    row_idx = idx // cols
                    col_idx = idx % cols
                    card[row_idx, col_idx] = 0

        result[f"card_{n}"] = card
    return result