import numpy as np

#################################################################################################################


def bingo_simulation(input_cards, num_simulations=100,pool = 75):

    bingo_results = np.zeros((num_simulations, pool))  # Each row represents a simulation, and each column represents the x+1th number called
    full_results = np.zeros((num_simulations, pool))    
    
    
    for sim in range(num_simulations):
    
        cards = cards = np.array(list(input_cards.values()))
        numbers_called = np.random.choice(np.arange(1,pool + 1), size = pool, replace = False) #random ordering of number based on the provided pool
        
        for num_called in range(len(numbers_called)):
            
            indices = np.where(cards == numbers_called[num_called])
            cards[indices] = 0
            
            bingos = np.sum(np.any(np.all(cards == 0, axis=2) | np.all(cards == 0, axis = 1), axis=1))

            fulls = np.sum(np.all(cards == 0, axis = (1,2)))
         

            bingo_results[sim][num_called] = bingos
            full_results[sim][num_called] = fulls
    
    print("done!")

    return bingo_results, full_results