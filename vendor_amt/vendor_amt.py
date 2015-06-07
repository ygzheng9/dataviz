
# imports needed for the following examples
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import scipy.spatial.distance as distance

# read a local file (path is relative to python's working directory)
# sep, header=True/None
infile = '../data/PO_asof_20150525.txt'
df = pd.read_table(infile, sep="|", thousands=',')

# set column name
df.columns = ['comp_code', 'comp_name', 'vendor_code', 'vendor_name',
              'which_day', 'po', 'amt']

grouped = df.groupby(['comp_code', 'vendor_code']).agg({'amt': np.sum,
                                                        'po': 'count'})
grouped['vendor_cnt'] = 1

grouped2 = grouped.groupby(level=0).agg({'amt': np.sum,
                                         'po': np.sum,
                                         'vendor_cnt': np.sum})

grouped2['amt_log'] = np.log2(grouped2['amt'])

fig2, ax2 = plt.subplots(nrows=1, ncols=2)
fig2.set_size_inches(24, 8)
plt.subplots_adjust(wspace=0.2)

grouped2.plot(kind='scatter', x='vendor_cnt', y='amt', ax=ax2[0],
              title='vendor count vs. amount')
ax2[0].set_xlabel('vendor count')
ax2[0].set_ylabel('toal amount')

grouped2.plot(kind='scatter', x='vendor_cnt', y='amt_log', ax=ax2[1],
              title='vendor count vs. log2(amount)')
ax2[1].set_xlabel('vendor count')
ax2[1].set_ylabel('total amount')

fig2.savefig('vendor_vs_amount.png')

plt.show()
