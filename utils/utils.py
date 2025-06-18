import duckdb
import streamlit as st
from streamlit.connections import ExperimentalBaseConnection

class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
    def _connect(self,**kwargs) -> duckdb.DuckDBPyConnection:
        motherduck_token = st.secrets['MOTHERDUCK_TOKEN']
        md_db_name = kwargs.get("md_db_name")
        
        #Read/Write
        connection_string = f"md:{md_db_name}?motherduck_token={motherduck_token}"
        return duckdb.connect(connection_string)

        #Read only
        # connection_string = f"md:{md_db_name}?session_hint=user123"
        # config = {"motherduck_token": f"{motherduck_token}"}
        # return duckdb.connect(connection_string, config=config, **kwargs)
    
con = DuckDBConnection(connection_name='test_con',md_db_name="sample_data")

    
