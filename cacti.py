def cacti_number(plot):   # cacti_number decorator

    moreCacti = 0  # Variable to store the count of additional cacti

    totalRows = len(plot)
    totalCols = len(plot[0])
    for row in range(totalRows):        # row
        for col in range(totalCols):    # column
            if plot[row][col] == 0:     # is cell empty?
                isAdjacent = False      # Let's assume a cacti can be planted here.
                
                # Check the four adjacent sides
                # If any of these four adjacent sides are true, can NOT plant at this cell
                if row > 0 and plot[row - 1][col] == 1:                 # Check upper cell
                    isAdjacent = True

                elif row < totalRows - 1 and plot[row + 1][col] == 1:   # check lower cell
                    isAdjacent = True

                elif col < totalCols - 1 and plot[row][col + 1] == 1:   # check right cell
                    isAdjacent = True

                elif col > 0 and plot[row][col - 1] == 1:               # check left cell
                    isAdjacent = True
                
                if isAdjacent == False:     # We can plant cacti here
                    plot[row][col] = 1      # need to assign 1 here, so don't duplicate 
                    moreCacti += 1          # increment count

    return moreCacti