# -*- coding: utf-8 -*-
"""
@Time    : 2017/11/26 下午12:02
@Author  : VincentGum
@File    : LOF.py
"""
import numpy as np


class LOF():
    DATA = np.array([1, 1])
    sample_number = 0  # numbers of all the samples
    k = 0
    dist_mode = 0  # 1 for Manhattan dist and 2 for Euclidean dist
    top = 0  # number of outliers you want to find out

    dist = np.array([1, 1])
    dist_k = np.array([1, 1])
    k_NN = {}
    lrd_k = np.array([1,1])
    LOF = []  # LOF for each point
    LOF_dict = {}  # having all the samples' indexs as keys and their LOF as values
    OUTLIERS_SET = {}  # having all the outliers, taking ontliers' indexs as keys and their LOF as values
    rd = []

    def __init__(self, DATA, k=2, dist_mode=1, top=1):
        """
        initial the class and input the parameter
        :param DATA: the points in which we want to handle and find out the outliers
        :param k: parameter k
        :param dist_mode: the way you want to calculate the distance, including Manhattan dist for Euclidean dist
        :param top: the numbers of outliers you want to output(k must be not exceeding the number of data points)
        """
        self.DATA = DATA
        self.k = k
        self.dist_mode = dist_mode
        self.top = top
        self.sample_number = DATA.shape[0]

    def l1_dist(self, point_1, point_2):
        """
        :param point_1: a vector like numeric data point, share a length with point_2
        :param point_2: a vector like numeric data point, share a length with point_1
        :return: the L1_norm(also called 'Manhattan') distance between two points
        """
        p_1 = np.array(point_1)
        p_2 = np.array(point_2)

        dist = np.sum(abs(p_1 - p_2))
        return dist

    def l2_dist(self, point_1, point_2):
        """
        :param point_1: a vector like numeric data point, share a length with point_2
        :param point_2: a vector like numeric data point, share a length with point_1
        :return: the L2_norm(also called 'Euclidean') distance between two points
        """
        p_1 = np.array(point_1)
        p_2 = np.array(point_2)

        dist = np.sum((p_1 - p_2) ** 2)
        return np.sqrt(dist)

    def build_distance_matrix(self):
        """
        calculate all the distances between each two data points, and build the 'distance' matrix
        :return: null, update the matrix 'distance'
        """
        # get the number of samples
        rows = self.DATA.shape[0]
        self.dist = np.zeros([rows, rows])

        # iterate to put number into the matrix
        for row in range(rows):
            for col in range(rows):

                # if it is asked to compute the Manhattan distance
                if self.dist_mode == 1:
                    self.dist[row, col] = self.l1_dist(self.DATA[row,], self.DATA[col,])

                # if it is asked to compute the Euclidean distance
                elif self.dist_mode == 2:
                    self.dist[row, col] = self.l2_dist(self.DATA[row,], self.DATA[col,])

    def cal_dist_k_o(self):
        """
        dist_k(o): distance between o and its k-th NN(k-th nearest neighbor)
        :return: fill the dist_k array like matrix with dist_k(o) for each sample
        """
        temp = []
        for i in range(self.sample_number):

            # take the corresponding row and sort it
            dists = sorted(list(self.dist[i, ]))
            temp.append(dists[self.k])

        self.dist_k = np.array(temp)

    def cal_kNN(self):
        """
        According to the dist_k(o), find out all the sample which is within the scope, and regard them as a neighborhood
        :return: fill a dictionary, having indexs for every sample for keys and the list containing
                their neighbor as value
        """
        for i in range(self.sample_number):
            self.k_NN[i] = []

        for row in range(self.sample_number):
            for col in range(self.sample_number):
                if (self.dist[row, col] <= self.dist_k[row]) and (row != col):
                    self.k_NN[row].append(col)

    def reachdist_k(self, o_, o):
        """
        calculate the reachdist_k for sample o
        :param o_:
        :param o:
        :return:
        """
        l = []
        l.append(self.dist_k[o_,])
        l.append(self.dist[o_, o])
        return max(l)

    def cal_lrd_k(self):
        """
        Calculate the lrd_k for every sample.
        :return:
        """
        temp = []
        for o in range(self.sample_number):
            down = 0
            for o_ in self.k_NN[o]:
                down += self.reachdist_k(o_, o)
            up = len(self.k_NN[o])
            temp.append(up / down)
            self.rd.append(down)

        self.lrd_k = np.array(temp)

    def cal_LOF_k(self):
        """
        calculate LOF
        :return: a list containing LOF for corresponding sample
        """
        temp = []

        for o in range(self.sample_number):
            down = len(self.k_NN[o])
            up = 0
            for o_ in self.k_NN[o]:
                up += (self.lrd_k[o_] / self.lrd_k[o])
            temp.append(up / down)
            self.LOF_dict[o] = up / down

        self.LOF = temp

    def get_outliers(self):
        """
        according to the given number 'top', put the samples with '#top' largest LOF in the dict
        :return:
        """
        temp = sorted(self.LOF, reverse=True)
        for i in range(self.top):
            self.OUTLIERS_SET[self.LOF.index(temp[i])] = ("%.3f" % temp[i])

    def scan(self):
        """
        do all the step above
        :return:
        """
        self.build_distance_matrix()
        self.cal_dist_k_o()
        self.cal_kNN()
        self.cal_lrd_k()
        self.cal_LOF_k()
        self.get_outliers()

