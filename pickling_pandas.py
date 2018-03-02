import pandas as pd
import quandl
import pickle
import matplotlib as plt
from matplotlib import pyplot


quandl.ApiConfig.api_key = '6uNRX8zyCfXpkY4xDHmg'
quandl.get('FMAC/30US', start_date='1999-02-22', end_date='2018-02-22')

##def ##state_list():
    ##fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
  ##  return fiddy_states[0][0][1:]
    
def get_initial_state_data():
    ##states = state_list()

    ##for abbv in states:
    query = "BCHARTS/ABUCOINSEUR"
    df = quandl.get(query, authtoken='6uNRX8zyCfXpkY4xDHmg')
    print('query is ' ,query)
    print (' df is ', df)

    del df['Volume (Currency)']

    
    HPI_data = pd.DataFrame()
    HPI_data.to_pickle('df.pickle')
    HPI_data2 = pd.read_pickle('df.pickle')
    print(HPI_data2) 
    
    df.plot()
    plt.pyplot.title('BITCOIN EXHANGE RATES')
    plt.pyplot.legend()
    plt.pyplot.show()
    

   ## pickle_out = open('fiddy_states.pickle','wb')
   ## pickle.dump(main_df, pickle_out)'
   ## pickle_out.close()

get_initial_state_data()


