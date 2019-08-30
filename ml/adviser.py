from sklearn.neighbors import NearestNeighbors
import numpy as np
import json
import numbers
from sklearn import decomposition
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
#X = np.array([[-1, -1, 1, 2], [-2, -1,3,4], [-3, -2, 2,5], [1, 1, 29, 40], [2, 1, 2,5], [3, 2, 6,3]])

def read_json(filename):
    with open(filename, 'r') as f:
        table = json.load(f)
    return table


class Adviser:
    def __init__(self, cor_file="cor_essence.json", bpm_file="bpm_essence.json", dump=True):
        self.cor_table = read_json(filename=cor_file)
        self.bpm_table = read_json(filename=bpm_file)

        self.get_atrb_from_cors_table()
        self.get_atrb_from_bpm_table(dump=dump)


    def find_mfiles(self, n_files, min_sase, cur_state, fit_db="kick"):
        db_indxs = self.get_indices(min_sase)
        if fit_db == "kick":
            fitting_data = self.cor_kicks[db_indxs]
        elif fit_db == "moment":
            fitting_data = self.cor_moments[db_indxs]
        elif fit_db == "orbit_x":
            fitting_data = self.bpm_X[db_indxs]
        elif fit_db == "orbit_y":
            fitting_data = self.bpm_Y[db_indxs]
        else:
            print("adviser error")
        print("fitting data is nan? ", fitting_data[np.isnan(fitting_data)])
        print("current data is nan? ",cur_state[np.isnan(cur_state)])
        indices = self.find_nearest_neighbors(n_neighbors=n_files, fitting_data=fitting_data, ref_data=cur_state)

        mf_list = self.get_info(indices, db_indxs)
        return mf_list

    def get_indices(self, min_sase):
        """
        Method to get indices of the sase array with condition sase_array > min_sase

        :param min_sase: sase level
        :return: indices
        """
        return np.where(self.sases > min_sase)[0]

    def find_nearest_neighbors(self, n_neighbors, fitting_data, ref_data):
        nbrs = NearestNeighbors(n_neighbors=n_neighbors, algorithm='ball_tree').fit(fitting_data)
        distances, indices = nbrs.kneighbors([ref_data])
        return indices[0]

    def get_info(self, indices, db_indxs):
        mf_list = []
        for i in indices:
            print(i, self.cor_ids[db_indxs][i], self.comments[db_indxs][i])
            mf_list.append({"id": self.cor_ids[db_indxs][i], "sase": self.sases[db_indxs][i],
                            "timestamp": self.timestamps[db_indxs][i],
                            "author": self.authors[db_indxs][i], "comment": self.comments[db_indxs][i]})
        return mf_list

    def get_atrb_from_cors_table(self):
        """
        sases         - array, one number for each machine file
        timestamps    - array, one number for each machine file
        cor_ids       - array, id of the machine file, one number for each machine file
        cor_kicks     - list of lists, one list for each machine file
        cor_moments   - list of lists, one list for each machine file
        cor_ref_names - list of corrector names

        :return:
        """
        self.sases = np.array(self.cor_table["sase"])
        self.timestamps = np.array(self.cor_table["timestamp"])
        self.cor_ids = np.array([float(x) for x in self.cor_table["ids"]])
        self.cor_kicks = np.array(self.cor_table["kicks"])
        self.cor_moments = np.array(self.cor_table["moments"]) if "moments" in self.cor_table else []
        self.cor_ref_names = self.cor_table["cor_names"]
        self.authors = np.array(self.cor_table["author"])
        self.comments = np.array(self.cor_table["comment"])

    def get_atrb_from_bpm_table(self, dump=True):
        """
        bpm_ids - array, id of the machine file, must be equal to self.cor_ids
        bpm_X   - list of lists, one list for each machine file
        bpm_Y   - list of lists, one list for each machine file
        :return:
        """
        self.bpm_ids = np.array([float(x) for x in self.bpm_table["ids"]])
        bpm_X = np.array(self.bpm_table["X"])
        bpm_Y = np.array(self.bpm_table["Y"])
        self.bpm_ref_names = self.bpm_table["bpm_names"]
        print("len", len(bpm_X))
        self.not_dump_indx = []
        if not dump:
            for name in self.bpm_ref_names:
                suff = name.split(".")[-1]
                if "D" not in suff:
                    self.not_dump_indx.append(True)
                else:
                    self.not_dump_indx.append(False)
        else:
            self.not_dump_indx = [True] * len(self.bpm_ref_names)
        self.bpm_X = []
        self.bpm_Y = []
        for i in range(len(bpm_X)):
            #print(self.bpm_X[i])
            self.bpm_X.append(bpm_X[i][self.not_dump_indx])
            self.bpm_Y.append(bpm_Y[i][self.not_dump_indx])
        
        self.bpm_X = np.array(self.bpm_X)
        self.bpm_Y = np.array(self.bpm_Y)
        #print(len(self.bpm_X ))
        self.bpm_ref_names = np.array(self.bpm_ref_names)[self.not_dump_indx]
        print("get_atrb_from_bpm_table: ", dump, len(self.bpm_ref_names ))




"""
table = read_json(filename="cor_essence.json")

sases = np.array(table["sase"])
timestamps = np.array(table["timestamp"])
ids = table["ids"]
all_kicks = table["kicks"]
all_moments = table["moments"]
ref_names = table["cor_names"]
indx = np.where(sases>100)[0]
print(len(indx))
nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(all_kicks)
distances, indices = nbrs.kneighbors([all_kicks[0]])
print(indices)
table_bpm = read_json(filename="bpm_essence.json")

ids_bpm = table_bpm["ids"]
X_bpm = table_bpm["X"]
Y_bpm = table_bpm["Y"]
bpm_ref_names = table_bpm["bpm_names"]
print(np.array_equal(ids_bpm, ids))
#print(k_means.labels_[::10])

#print(sases[::10])



#iris = datasets.load_iris()
#X_iris = iris.data
#y_iris = iris.target
#X = np.array(all_kicks)[indx]
X = np.array(X_bpm)[indx]
times = np.array(timestamps)[indx]
sase = sases[indx]
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X)
print(k_means.labels_)
y = k_means.labels_
pca = decomposition.PCA()

print(times[y==2])
for i in range(3):
    x = sase[y==i]
    print(np.min(x), np.max(x))
pca.fit(X)


#print(pca.explained_variance_)


# As we can see, only the 2 first components are useful
pca.n_components = 2


X_reduced = pca.fit_transform(X)

#print(X_reduced.shape)


plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)
#colors = get_cmap(7)
#print(colors)
for i, color in zip([0,1,2], colors):
    plt.scatter(X_reduced[y==i, 0], X_reduced[y==i, 1], color=colors[i], alpha=.8, lw=lw)
#plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of Correctors dataset')
plt.show()
"""