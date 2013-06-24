from disco.job import Job
from disco.worker.classic.func import chain_reader
from disco.core import result_iterator

from disco.worker.classic.func import nop_map

class WikiTime(Job):

    partitions = 3
    input=['tag://h5:wiki:log']
    
    map = staticmethod(nop_map)

    @staticmethod
    def map_reader(input_fd, size, url, params):
        from cStringIO import StringIO
        import os
        import pandas as pd

        fd = input_fd
        if not hasattr(fd, 'name'):
            # Sometimes disco might give you a handle to a file on another
            # node -- to satisfy h5py.File() below, pull that file down to
            # the local node (storing it on the virtual disk present on
            # many Linux systems at /dev/shm/) for subsequent reading.
            import tempfile
            temp_fd = tempfile.NamedTemporaryFile(prefix="/dev/shm/disco")
            temp_fd.write(fd.read())
            temp_fd.flush()
            fd = temp_fd

        from datetime import datetime
        time =  url.split('/')[-1]
        day = time.split('-')[1]
        hour = time.split('-')[2].split('_')[0]

        date = datetime.strptime(day+'-'+hour,'%Y%m%d-%H%M%S')
        
        
        
        file_hdf5 = h5py.File(fd.name, 'r')
        keys = file_hdf5.keys()[0]

        data = file_hdf5[keys]['project_code','views']
        df = pd.DataFrame(data)
        
        
        filtered = df[df['project_code'].isin(['en','fr'])]
        sumProject = filtered.groupby('project_code').views.sum()
        
        #sumProject is a Pandas Series
        sumProject.name=[date.isoformat()]
        print sumProject

        yield date, sumProject


if __name__ == "__main__":
    from wiki_log import WikiTime
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    wikitime = WikiTime().run()
    
    dfDateList = []

    for (date, df) in result_iterator(wikitime.wait(show=True)):
        print date,df
        dfDateList.append((date, df))

    #sort list by time
    dfSortedDateList = sorted(dfDateList, key=lambda x: x[0])

    #create combined dataframe
    new_df = pd.DataFrame(dfSortedDateList[0][1])
    for i in np.arange(1,len(dfSortedDateList)):
        print i
        new_df = new_df.join(pd.DataFrame(dfSortedDateList[i][1]))



    def divideByMax(group):
        maxVal = np.max(group)
        return group/float(maxVal)


    print new_df.apply(divideByMax,axis=1) # apply function to each row

    normalized = new_df.apply(divideByMax,axis=1)

    ax = plt.gca()
    ax = normalized.T.plot(rot=20,fontsize='8')
    ax.set_xticklabels([str(x) for x in range(0,24,6)])
    proj1 = normalized.T.columns.values[0]
    proj2 = normalized.T.columns.values[1]
    ax.set_title
    ax.grid(True)
    plt.savefig(proj1+'_and_'+proj2+'.png')


