def get_ratings_tuple(entry):
    items = entry.split('::')
    return int(items[0]), int(items[1]), float(items[2])


def get_movie_tuple(entry):
    items = entry.split('::')
    return int(items[0]), items[1]

import sys
import os

baseDir = os.path.join('/data')
inputPath = os.path.join('12', '5')

ratingsFilename = os.path.join(baseDir, inputPath, 'ratings.dat.gz')
moviesFilename = os.path.join(baseDir, inputPath, 'movies.dat')

numPartitions = 2
rawRatings = sc.textFile(ratingsFilename).repartition(numPartitions)

rawMovies = sc.textFile(moviesFilename)

ratingsRDD = rawRatings.map(get_ratings_tuple).cache()
moviesRDD = rawMovies.map(get_movie_tuple).cache()

ratingsCount = ratingsRDD.count()

moviesCount = moviesRDD.count()

print 'There are %s ratings and %s movies in the datasets' % (ratingsCount, moviesCount)

print 'Ratings: %s' % ratingsRDD.take(3)

print 'Movies: %s' % moviesRDD.take(3)

def sortFunction(tuple):
    key = unicode('%.3f' % tuple[0])
    value = tuple[1]
    return (key + ' ' + value)

def getCountsAndAverages(IDandRatingsTuple):
    ratingsCount = len(IDandRatingsTuple[1])
    ratingsSum = float(sum(IDandRatingsTuple[1]))
    return (IDandRatingsTuple[0], (ratingsCount, ratingsSum / ratingsCount))

getCountsAndAverages((1, (1, 2, 3, 4)))

movieIDsWithRatingsRDD = (ratingsRDD
                          .map(lambda x : (x[1], x[2]))
                          .groupByKey())
movieIDsWithRatingsRDD.take(3)
print 'movieIDsWithRatingsRDD: %s\n' % movieIDsWithRatingsRDD.take(3)

movieIDsWithAvgRatingsRDD = movieIDsWithRatingsRDD.map(getCountsAndAverages)
print 'movieIDsWithAvgRatingsRDD: %s\n' % movieIDsWithAvgRatingsRDD.take(3)

movieNameWithAvgRatingsRDD = (moviesRDD
                              .join(movieIDsWithAvgRatingsRDD)
                              .map(lambda x : (x[1][1][1], x[1][0], x[1][1][0])))
print 'movieNameWithAvgRatingsRDD: %s\n' % movieNameWithAvgRatingsRDD.take(3)

movieLimitedAndSortedByRatingRDD = (movieNameWithAvgRatingsRDD
                                    .filter(lambda x : x[2] > 500)
                                    .sortBy(sortFunction, False))

print 'Movies with highest ratings: %s' % movieLimitedAndSortedByRatingRDD.take(20)

trainingRDD, validationRDD, testRDD = ratingsRDD.randomSplit([6, 2, 2], seed=0L)

print 'Training: %s, validation: %s, test: %s\n' % (trainingRDD.count(),
                                                    validationRDD.count(),
                                                    testRDD.count())

import math

def computeError(predictedRDD, actualRDD):
    predictedReformattedRDD = predictedRDD.map(lambda x : ((x[0], x[1]), x[2]))
    actualReformattedRDD = actualRDD.map(lambda x : ((x[0], x[1]), x[2]))
    squaredErrorsRDD = (predictedReformattedRDD
                        .join(actualReformattedRDD)
                        .map(lambda x : (x[1][0] - x[1][1]) ** 2))
    totalError = squaredErrorsRDD.sum()
    numRatings = squaredErrorsRDD.count()
    return math.sqrt(float(totalError) / numRatings)

testPredicted = sc.parallelize([
    (1, 1, 5),
    (1, 2, 3),
    (1, 3, 4),
    (2, 1, 3),
    (2, 2, 2),
    (2, 3, 4)])
testActual = sc.parallelize([
     (1, 2, 3),
     (1, 3, 5),
     (2, 1, 5),
     (2, 2, 1)])
testError = computeError(testPredicted, testActual)

print 'Error for test dataset: %s' % testError

from pyspark.mllib.recommendation import ALS

validationForPredictRDD = validationRDD.map(lambda x : (x[0], x[1]))

seed = 5L
iterations = 5
regularizationParameter = 0.1
ranks = [4, 8, 12]
errors = [0, 0, 0]
err = 0
tolerance = 0.03

minError = float('inf')
bestRank = -1
bestIteration = -1
for rank in ranks:
    model = ALS.train(trainingRDD, rank, seed=seed, iterations=iterations,
                      lambda_=regularizationParameter)
    predictedRatingsRDD = model.predictAll(validationForPredictRDD)
    error = computeError(predictedRatingsRDD, validationRDD)
    errors[err] = error
    err += 1
    print 'For rank %s the RMSE is %s' % (rank, error)
    if error < minError:
        minError = error
        bestRank = rank


print 'The best model was trained with rank %s' % bestRank

myModel = ALS.train(trainingRDD, ranks[2], seed=seed, iterations=iterations,
                    lambda_=regularizationParameter)

testForPredictingRDD = testRDD.map(lambda x : (x[0], x[1]))
predictedTestRDD = myModel.predictAll(testForPredictingRDD)
testRMSE = computeError(testRDD, predictedTestRDD)
print 'The model had a RMSE on the test set of %s' % testRMSE

trainingAvgRating = trainingRDD.map(lambda x : x[2]).sum() / float(trainingRDD.map(lambda x : x[2]).count())
print 'The average rating for movies in the training set is %s' % trainingAvgRating

testForAvgRDD = testRDD.map(lambda x : (x[0], x[1], trainingAvgRating))
testAvgRMSE = computeError(testRDD, testForAvgRDD)
print 'The RMSE on the average set is %s' % testAvgRMSE