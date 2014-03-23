Title: Test of code blocks
Date: 2014-03-21 10:20
Category: Test
Summary: Test to see where summary shows up.

This is the content of my super blog post.

Testing Python code:

    :::python
    import multiprocessing as mp
    pool = mp.Pool(3)
    import numpy as np
    pool.map(np.sqrt, [0,1,2,3,4])
    for boop in boops:
    	print(boop)

Testing R code:

	:::r
	library(randomForest)
	d <- read.csv('file.csv')
	ggplot(data=d) +
		geom_point(aes(x=x, y=y))
