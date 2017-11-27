This is a simple class for detecting outliers using LOF

1, Initiate a LOF class like this:

    'lof = LOF.LOF(DATA, k=2, dist_mode=1, top=1)'
                    |     |           |_____  |______ the number of
                    /     |                 |  outliers you want to detect
                   / size of neighborhood   |
                  /                         |
     a 'np.array' data set,             1 for Manhattan
     having each row for a sample          2 for Euclidean
     and each col for a attribute

2, After initiating the lof class, detect the outliers like this:

    'lof.scan()'

    it would run a series of function to do the job.

3, Then, you can call for some variables:

    'lof.dist' for distance between all the samples;
    'lof.k_NN' for all the neighbors for every samples, give a dictionary, sample index for keys, lists containing neighbors for values;
    'lof.LOF'  for all the LOF for all the samples
    'lof.OUTLIERS_SET' for all outliers you want, give a dictionary, sample index for keys and LOF for values;