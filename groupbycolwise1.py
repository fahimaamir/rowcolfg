import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from collections import defaultdict
#from st_aggrid.shared import getAllColumnProps, getAllGridOptions
#from st_aggrid import getAllColumnProps, getAllGridOptions
from st_aggrid import AgGrid, GridOptionsBuilder


def generate_sales_data():
        """Generate dataset simulating sales data."""
        np.random.seed(42)
        rows = 50

        # Create a more complex dataset
        df = pd.DataFrame({
            'Product_ID': range(1, rows + 1),
            'City': np.random.choice(['Karachi', 'Islamabad', 'Quata', 'Pishawar'], rows),
            'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], rows),
            'Sale_person': np.random.choice(['Fahim', 'Aamir', 'Zahir', 'Asim'], rows),
            'Base_Price': np.random.uniform(10, 500, rows).round(2),
            'Quantity_Sold': np.random.randint(1, 100, rows),
            'commission': np.random.randint(100, 1000, rows),
        })

        return df


def configure_grid_options(df):
        """Configure advanced grid options with multiple features."""
        gb = GridOptionsBuilder.from_dataframe(df)
        # Configure row grouping and aggregation
        gb.configure_column("allColumns", filter=True)
        for column in df.columns:
            gb.configure_column(column, filter=True)

        gb.configure_default_column(
                    groupable=True,
                    value=True,
                    enableRowGroup=True,
                    aggFunc='sum'
                )

                # Add filter and sort options
        gb.configure_grid_options(
                    enableRangeSelection=True,
                    enableRangeHandle=True,
                    suppressColumnMoveAnimation=False,
                    suppressRowClickSelection=False
                )
        
        return gb.build()
sales_data = generate_sales_data()

grid_options = configure_grid_options(sales_data)
gb = GridOptionsBuilder()
gb.configure_default_column( groupable=True,value=True,enableRowGroup=True,aggFunc='sum'  )

                # Add filter and sort options
gb.configure_grid_options(
                    enableRangeSelection=True,
                    enableRangeHandle=True,
                    allColumnsfilter=True,
                    #gob.configure_column("allColumns", filter=True)
                    suppressColumnMoveAnimation=False,
                    suppressRowClickSelection=False)
gb.build()

        

    #st.subheader('Interactive Sales Data Grid')
st.markdown("""
    **Features:**
    - Edit Base Price and Quantity Sold
    - Automatic Total Revenue calculation
    """)





    # AgGrid with custom options
mfa = AgGrid(
        sales_data,
        gridOptions=grid_options,
        height=500,
        theme='alpine',
        allow_unsafe_jscode=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        #update_mode=GridUpdateMode.GRID_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=True,
        width =2900 ,
        reload_data=False
    )


if st.button('Check availability'):
    st.write(mfa['data'])
    mfa4 =mfa['data']
    st.write(mfa['columns_state'])
    fild = pd.DataFrame(mfa['columns_state'])
    #fild2= fild[["colid"]]
    st.write(fild)
    
    #above_35= fild[fild["hide"] == 'False']
    #above_35= fild["hide"] 
    #above_36= fild["colId"] 
    #st.write(above_35)
    #st.write(above_36)
    #list_from_df = above_36.values.tolist()
    #list_from_column = df['numbers'].tolist()
    #list_from_column = fild["colId"].tolist()
    #st.write(above_36.to_string(index=False))
    #st.write(list_from_df)
    #st.write(list_from_column)
    
    #fild["hide"] = fild["hide"].astype(int) 
    #fild = fild[fild["hide"]==0 ]
    #list_from_df2 = fild["colId"].values.tolist()
    #st.write("muhammad is the best ")
    #st.write(fild)
    #st.write(list_from_df2)
    
    #mfa5 = mfa4[list_from_column]
    #mfa6 = mfa4[list_from_df2]
    
    #st.write(mfa5)
    #st.write(mfa6)